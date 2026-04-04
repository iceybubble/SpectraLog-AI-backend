from fastapi import APIRouter
from app.models.schemas import XAIExplanation

router = APIRouter(prefix="/xai", tags=["xai"])


@router.get("/explain/{alert_id}", response_model=XAIExplanation)
async def explain_alert(alert_id: str):
    """Get XAI explanation for why alert was triggered"""
    
    return {
        "alert_id": alert_id,
        "model": "Isolation Forest",
        "features": [
            {
                "name": "login_failures",
                "value": 15,
                "impact": 0.85,
                "explanation": "High number of failed login attempts indicates brute force attack",
            },
            {
                "name": "unusual_time",
                "value": "03:45 AM",
                "impact": 0.65,
                "explanation": "Activity during unusual hours increases suspicion",
            },
            {
                "name": "unknown_ip",
                "value": "45.142.212.61",
                "impact": 0.78,
                "explanation": "IP address not in whitelist and from high-risk region",
            },
            {
                "name": "rapid_requests",
                "value": 50,
                "impact": 0.72,
                "explanation": "Unusually high request rate suggests automated attack",
            },
        ],
        "confidence": 0.92,
        "reasoning": "This alert was triggered due to multiple high-impact anomalies including excessive failed login attempts, activity during unusual hours, and requests from a suspicious IP address.",
    }