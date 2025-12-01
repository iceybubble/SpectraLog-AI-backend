from datetime import datetime
import uuid

from fastapi import APIRouter, HTTPException

from app.models.log_event import LogEvent
from app.core.elastic import es, INDEX_PREFIX

router = APIRouter()

@router.post("/ingest")
async def ingest_log(event: LogEvent):
    # Transform incoming event into a format suitable for Elasticsearch
    doc = {
        "@timestamp": event.timestamp.isoformat(),
        "device_type": event.device_type,
        "device_id": event.device_id,
        "event_type": event.event_type,
        "severity": event.severity,
        "message": event.message,
        "details": event.details,
        "ingest_id": str(uuid.uuid4()),
        "ingested_at": datetime.utcnow().isoformat(),
    }

    # ES index name e.g. spectralog-2025.12.01
    index_name = f"{INDEX_PREFIX}-{event.timestamp.strftime('%Y.%m.%d')}"

    try:
        res = es.index(index=index_name, document=doc)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to index document: {e}")

    return {"status": "indexed", "index": index_name, "id": res.get('_id')}
