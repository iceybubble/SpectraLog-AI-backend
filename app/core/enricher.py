# app/core/enricher.py

import ipaddress
from typing import Dict, Any


class LogEnricher:
    """
    Adds contextual intelligence to normalized logs
    without modifying original evidence.
    """

    @staticmethod
    def enrich(event: Dict[str, Any]) -> Dict[str, Any]:
        """
        Enrich a normalized event with contextual metadata.
        """

        enrichment = {}

        # --- IP ENRICHMENT ---
        ip = event.get("parsed_fields", {}).get("ip")
        if ip:
            enrichment["ip_context"] = LogEnricher._enrich_ip(ip)

        # --- DEVICE ENRICHMENT ---
        source_type = event.get("source_type", "unknown")
        enrichment["device_context"] = {
            "type": source_type,
            "risk": LogEnricher._device_risk(source_type),
        }

        # Attach enrichment without destroying evidence
        event["enrichment"] = enrichment
        return event

    @staticmethod
    def _enrich_ip(ip: str) -> Dict[str, Any]:
        try:
            ip_obj = ipaddress.ip_address(ip)
            return {
                "is_private": ip_obj.is_private,
                "is_loopback": ip_obj.is_loopback,
                "geo": "local" if ip_obj.is_private else "external",
            }
        except ValueError:
            return {"invalid_ip": True}

    @staticmethod
    def _device_risk(source_type: str) -> str:
        if source_type in {"server", "cloud"}:
            return "medium"
        if source_type in {"android", "iot"}:
            return "low"
        return "unknown"
