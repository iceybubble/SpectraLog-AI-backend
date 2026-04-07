from fastapi import APIRouter, Query, HTTPException
from typing import Optional, Any, Dict, List
from datetime import datetime
from app.models.schemas import PaginatedResponse, Log, LogSearchBody

router = APIRouter(prefix="/logs", tags=["logs"])

def _mock_logs() -> List[Dict[str, Any]]:
    return [
        {
            "id": f"log-{i}",
            "timestamp": datetime.now().isoformat(),
            "source": "windows" if i % 2 == 0 else "android",
            "severity": "info" if i % 3 else "warning",
            "event_type": "login",
            "message": f"User login attempt {i}",
            "device_id": "DESKTOP-001" if i % 2 == 0 else "Android-Phone-01",
            "user": "admin",
            "ip_address": "192.168.1.100",
            "metadata": {"attempt": i},
        }
        for i in range(1, 41)
    ]


@router.get("/", response_model=PaginatedResponse)
async def get_logs(
    source: Optional[str] = None,
    severity: Optional[str] = None,
    limit: int = Query(100, le=1000),
    offset: int = 0,
):
    logs = _mock_logs()
    if source:
        logs = [log for log in logs if log["source"] == source]
    if severity:
        logs = [log for log in logs if log["severity"] == severity]

    return {
        "items": logs[offset: offset + limit],
        "total": len(logs),
        "page": offset // limit + 1,
        "size": limit,
        "pages": (len(logs) + limit - 1) // limit,
    }


@router.get("/{log_id}", response_model=Log)
async def get_log_detail(log_id: str):
    for log in _mock_logs():
        if log["id"] == log_id:
            return log

    raise HTTPException(status_code=404, detail="Log not found")


@router.post("/search", response_model=PaginatedResponse)
async def search_logs(search_body: LogSearchBody):
    logs = _mock_logs()

    if search_body.query:
        q = search_body.query.lower()
        logs = [
            log for log in logs
            if q in log["message"].lower() or q in log["event_type"].lower()
        ]

    if search_body.filters:
        for key, value in search_body.filters.items():
            logs = [log for log in logs if log.get(key) == value]

    limit = search_body.limit
    offset = search_body.offset
    return {
        "items": logs[offset: offset + limit],
        "total": len(logs),
        "page": offset // limit + 1,
        "size": limit,
        "pages": (len(logs) + limit - 1) // limit,
    }