from fastapi import APIRouter

router = APIRouter(prefix="/enrichment", tags=["enrichment"])


@router.get("/ip/{ip}")
async def get_ip_info(ip: str):
    """Return basic enrichment details for an IP."""
    return {
        "ip": ip,
        "country": "Unknown",
        "city": "Unknown",
        "asn": "AS0",
        "reputation": "unknown",
        "is_vpn": False,
        "is_tor": False,
    }


@router.get("/threat-intel/{indicator}")
async def get_threat_intel(indicator: str):
    """Return mock threat intel hits for an indicator."""
    return {
        "indicator": indicator,
        "type": "unknown",
        "hits": 0,
        "confidence": 0.0,
        "sources": [],
        "verdict": "no_known_match",
    }
