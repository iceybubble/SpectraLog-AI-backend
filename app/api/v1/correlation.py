from fastapi import APIRouter
from typing import Optional, List
from datetime import datetime
from models.schemas import TimelineEvent, CorrelationGraph

router = APIRouter(prefix="/correlation", tags=["correlation"])


@router.get("/timeline", response_model=List[TimelineEvent])
async def get_timeline(
    start_time: str,
    end_time: str,
    source: Optional[str] = None,
):
    """Get events for timeline visualization"""
    
    return [
        {
            "timestamp": datetime.now().isoformat(),
            "device": "DESKTOP-001",
            "event": "Failed Login",
            "severity": 3,
            "source": "windows",
            "details": "5 consecutive failed attempts",
        },
        {
            "timestamp": datetime.now().isoformat(),
            "device": "Android-Phone-01",
            "event": "Suspicious App Install",
            "severity": 2,
            "source": "android",
            "details": "Unknown app installation detected",
        },
        {
            "timestamp": datetime.now().isoformat(),
            "device": "SERVER-PROD-01",
            "event": "Unauthorized Access",
            "severity": 4,
            "source": "server",
            "details": "Root access attempt from unknown IP",
        },
    ]


@router.get("/graph/{alert_id}", response_model=CorrelationGraph)
async def get_correlation_graph(alert_id: str):
    """Get event correlation graph for specific alert"""
    
    return {
        "nodes": [
            {"id": "ip-1", "type": "ip", "label": "192.168.1.100", "risk_score": 0.8},
            {"id": "device-1", "type": "device", "label": "DESKTOP-001", "risk_score": 0.6},
            {"id": "user-1", "type": "user", "label": "admin", "risk_score": 0.3},
            {"id": "process-1", "type": "process", "label": "powershell.exe", "risk_score": 0.7},
        ],
        "edges": [
            {"source": "ip-1", "target": "device-1", "relationship": "connected_to", "weight": 0.9},
            {"source": "device-1", "target": "user-1", "relationship": "logged_in_as", "weight": 0.8},
            {"source": "user-1", "target": "process-1", "relationship": "executed", "weight": 0.7},
        ],
    }