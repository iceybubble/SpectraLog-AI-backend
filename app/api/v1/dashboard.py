from fastapi import APIRouter
from app.models.schemas import DashboardMetrics
from app.core.elastic import get_es_client

router = APIRouter(prefix="/dashboard", tags=["dashboard"])


@router.get("/metrics", response_model=DashboardMetrics)
async def get_metrics():
    """Get dashboard metrics from Elasticsearch"""
    
    try:
        es = get_es_client()
        
        # Count total logs
        total_logs = es.count(index="logs-*", request_timeout=1)["count"]
        
        # Count total alerts
        total_alerts = es.count(index="alerts-*", request_timeout=1)["count"]
        
        # Count critical alerts
        critical_alerts_result = es.count(
            index="alerts-*",
            query={"term": {"severity": "critical"}},
            request_timeout=1,
        )
        critical_alerts = critical_alerts_result["count"]
        
        # Count open investigations
        open_investigations = es.count(
            index="alerts-*",
            query={"term": {"status": "investigating"}},
            request_timeout=1,
        )["count"]
        
        # TODO: Calculate devices_monitored from unique device_ids
        devices_monitored = 156
        
        # TODO: Calculate threat_score based on your algorithm
        threat_score = 7.8
        
        return {
            "total_logs": total_logs,
            "total_alerts": total_alerts,
            "critical_alerts": critical_alerts,
            "open_investigations": open_investigations,
            "devices_monitored": devices_monitored,
            "threat_score": threat_score,
        }
    
    except Exception as e:
        # Fallback to mock data
        return {
            "total_logs": 125847,
            "total_alerts": 342,
            "critical_alerts": 23,
            "open_investigations": 12,
            "devices_monitored": 156,
            "threat_score": 7.8,
        }