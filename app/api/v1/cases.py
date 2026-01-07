# app/api/v1/cases.py

from fastapi import APIRouter, HTTPException
from typing import Dict, Any

from app.models.case import Case
from app.core.elastic import get_es_client

router = APIRouter(prefix="/cases", tags=["Cases"])


@router.post("/")
def create_case(payload: Dict[str, Any]):
    """
    Create a new investigation case.
    """

    title = payload.get("title")
    if not title:
        raise HTTPException(status_code=400, detail="Case title is required")

    description = payload.get("description", "")
    created_by = payload.get("created_by", "system")

    case = Case(
        title=title,
        description=description,
        created_by=created_by,
    )

    case_data = case.to_dict()

    try:
        es = get_es_client()
        es.index(index="cases", id=case.case_id, document=case_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {
        "status": "success",
        "case": case_data,
    }
@router.get("/{case_id}")
def get_case(case_id: str):
    """
    Retrieve a case by ID.
    """

    try:
        es = get_es_client()
        result = es.get(index="cases", id=case_id)
        return {
            "status": "success",
            "case": result["_source"],
        }
    except Exception:
        raise HTTPException(status_code=404, detail="Case not found")

@router.post("/{case_id}/attach-event")
def attach_event_to_case(case_id: str, payload: Dict[str, Any]):
    """
    Attach an event to an existing case.
    """

    event_id = payload.get("event_id")
    if not event_id:
        raise HTTPException(status_code=400, detail="event_id is required")

    try:
        es = get_es_client()

        # Fetch case
        case_doc = es.get(index="cases", id=case_id)
        case_data = case_doc["_source"]

        # Attach event
        if event_id not in case_data["events"]:
            case_data["events"].append(event_id)

        # Update case
        es.index(index="cases", id=case_id, document=case_data)

        return {
            "status": "success",
            "case_id": case_id,
            "attached_event": event_id,
        }

    except Exception:
        raise HTTPException(status_code=404, detail="Case not found")

@router.get("/{case_id}/timeline")
def get_case_timeline(case_id: str):
    """
    Reconstruct a chronological timeline of events for a case.
    """

    try:
        es = get_es_client()

        # 1️⃣ Fetch the case
        case_doc = es.get(index="cases", id=case_id)
        case_data = case_doc["_source"]

        event_ids = case_data.get("events", [])
        if not event_ids:
            return {
                "status": "success",
                "case_id": case_id,
                "timeline": [],
                "message": "No events attached to this case"
            }

        # 2️⃣ Fetch all events linked to the case
        events = []
        for eid in event_ids:
            try:
                ev = es.get(index="logs-events", id=eid)
                events.append(ev["_source"])
            except Exception:
                continue  # skip missing/tampered events safely

        # 3️⃣ Sort events by timestamp
        events.sort(key=lambda e: e.get("timestamp", ""))

        # 4️⃣ Build forensic timeline
        timeline = []
        for idx, event in enumerate(events, start=1):
            timeline.append({
                "step": idx,
                "timestamp": event.get("timestamp"),
                "event_type": event.get("event_type"),
                "action": event.get("action"),
                "source_type": event.get("source_type"),
                "severity": event.get("severity"),
                "summary": event.get("explanation", {}).get("summary"),
                "confidence": event.get("explanation", {}).get("confidence"),
                "event_id": event.get("event_id"),
            })

        return {
            "status": "success",
            "case_id": case_id,
            "title": case_data.get("title"),
            "timeline": timeline
        }

    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
