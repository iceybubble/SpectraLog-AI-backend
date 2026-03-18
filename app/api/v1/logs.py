from fastapi import APIRouter, Query
from typing import Optional
from datetime import datetime
from app.models.schemas import PaginatedResponse

router = APIRouter(prefix="/logs", tags=["logs"])

@router.get("/", response_model=PaginatedResponse)
async def get_logs(
    source: Optional[str] = None,
    severity: Optional[str] = None,
    limit: int = Query(100, le=1000),
    offset: int = 0,
):
    mock_logs = [
        {
            "id": f"log-{i}",
            "timestamp": datetime.now().isoformat(),
            "source": "windows",
            "severity": "info",
            "event_type": "login",
            "message": f"User login attempt {i}",
            "device_id": "DESKTOP-001",
            "user": "admin",
            "ip_address": "192.168.1.100",
        }
        for i in range(1, 21)
    ]

    return {
        "items": mock_logs[offset: offset + limit],
        "total": len(mock_logs),
        "page": offset // limit + 1,
        "size": limit,
        "pages": (len(mock_logs) + limit - 1) // limit,
    }