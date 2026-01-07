# app/core/anomaly.py

from datetime import datetime
from typing import Dict, Any, List


class AnomalyDetector:
    """
    Explainable, rule-based anomaly detection engine.
    """

    @staticmethod
    def analyze(event: Dict[str, Any]) -> Dict[str, Any]:
        reasons: List[str] = []
        score = 0.0

        # --- Rule 1: Severity-based suspicion ---
        severity = event.get("severity", "low")
        if severity in {"high", "critical"}:
            reasons.append(f"High severity event: {severity}")
            score += 0.4

        # --- Rule 2: Unusual hour activity ---
        try:
            hour = datetime.fromisoformat(event["timestamp"]).hour
            if hour < 5 or hour > 23:
                reasons.append("Activity occurred at unusual hour")
                score += 0.2
        except Exception:
            pass

        # --- Rule 3: External IP for sensitive actions ---
        enrichment = event.get("enrichment", {})
        ip_ctx = enrichment.get("ip_context", {})
        if ip_ctx.get("geo") == "external" and event.get("event_type") == "auth":
            reasons.append("Authentication attempt from external IP")
            score += 0.3

        # --- Rule 4: Unknown device ---
        device_ctx = enrichment.get("device_context", {})
        if device_ctx.get("risk") == "unknown":
            reasons.append("Unknown or unclassified device source")
            score += 0.1

        is_anomalous = score >= 0.5

        event["anomaly"] = {
            "is_anomalous": is_anomalous,
            "score": round(score, 2),
            "reasons": reasons,
        }

        return event
