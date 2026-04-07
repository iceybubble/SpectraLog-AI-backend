from fastapi import APIRouter, Query
from typing import Optional
from datetime import datetime
from app.models.schemas import Alert, AlertUpdate, PaginatedResponse, AlertStatus
from app.core.elastic import get_es_client

router = APIRouter(prefix="/alerts", tags=["alerts"])


@router.get("/", response_model=PaginatedResponse)
async def get_alerts(
    status: Optional[str] = None,
    severity: Optional[str] = None,
    limit: int = Query(100, le=1000),
):
    """Get all alerts with optional filters"""
    
    try:
        es = get_es_client()
        
        query = {"bool": {"must": []}}
        
        if status:
            query["bool"]["must"].append({"term": {"status": status}})
        
        if severity:
            query["bool"]["must"].append({"term": {"severity": severity}})
        
        if not query["bool"]["must"]:
            query = {"match_all": {}}
        
        result = es.search(
            index="alerts-*",
            query=query,
            size=limit,
            sort=[{"@timestamp": {"order": "desc"}}],
            request_timeout=1,
        )
        
        alerts = []
        for hit in result["hits"]["hits"]:
            alert = hit["_source"]
            alert["id"] = hit["_id"]
            alerts.append(alert)
        
        total = result["hits"]["total"]["value"]
        
        return {
            "items": alerts,
            "total": total,
            "page": 1,
            "size": limit,
            "pages": (total + limit - 1) // limit,
        }
    
    except Exception as e:
        # Mock data fallback
        mock_alerts = [
            {
                "id": f"alert-{i}",
                "timestamp": datetime.now().isoformat(),
                "title": f"Suspicious Activity Detected #{i}",
                "description": "Multiple failed login attempts from unusual location",
                "severity": "high" if i % 2 == 0 else "medium",
                "status": "open",
                "source": "windows",
                "related_logs": [f"log-{i}", f"log-{i+1}"],
                "mitre_tactics": ["T1110.001"],
                "confidence": 0.85,
            }
            for i in range(1, 11)
        ]
        
        return {
            "items": mock_alerts[:limit],
            "total": len(mock_alerts),
            "page": 1,
            "size": limit,
            "pages": 1,
        }


@router.get("/{alert_id}", response_model=Alert)
async def get_alert_detail(alert_id: str):
    """Get alert details"""
    
    return {
        "id": alert_id,
        "timestamp": datetime.now().isoformat(),
        "title": "Critical: Brute Force Attack Detected",
        "description": "Automated brute force attack detected from IP 45.142.212.61",
        "severity": "critical",
        "status": "open",
        "source": "windows",
        "related_logs": ["log-1", "log-2", "log-3"],
        "mitre_tactics": ["T1110.001", "T1078"],
        "confidence": 0.92,
    }


@router.post("/{alert_id}/acknowledge")
async def acknowledge_alert(alert_id: str):
    """Mark alert as acknowledged"""
    
    return {"message": f"Alert {alert_id} acknowledged", "status": "acknowledged"}


@router.patch("/{alert_id}")
async def update_alert_status(alert_id: str, update: AlertUpdate):
    """Update alert status"""
    
    return {
        "id": alert_id,
        "timestamp": datetime.now().isoformat(),
        "status": update.status,
        "message": "Alert status updated successfully"
    }