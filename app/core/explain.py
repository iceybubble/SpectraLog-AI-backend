# app/core/explain.py

from typing import Dict, Any, List


class ExplainabilityEngine:
    """
    Converts anomaly detection results into
    human-readable forensic explanations.
    """

    @staticmethod
    def explain(event: Dict[str, Any]) -> Dict[str, Any]:
        explanations: List[str] = []

        anomaly = event.get("anomaly", {})
        enrichment = event.get("enrichment", {})

        # --- Anomaly-based explanations ---
        if anomaly.get("is_anomalous"):
            for reason in anomaly.get("reasons", []):
                explanations.append(reason)
        else:
            explanations.append("Event behavior is within normal baseline")

        # --- Contextual explanations ---
        ip_ctx = enrichment.get("ip_context", {})
        if ip_ctx.get("geo") == "external":
            explanations.append("Source IP is external to the trusted network")

        if ip_ctx.get("is_private"):
            explanations.append("Source IP belongs to a private/internal network")

        device_ctx = enrichment.get("device_context", {})
        if device_ctx.get("risk") == "unknown":
            explanations.append("Device source has not been previously classified")

        # --- Final forensic explanation ---
        event["explanation"] = {
            "summary": ExplainabilityEngine._build_summary(event),
            "details": explanations,
            "confidence": ExplainabilityEngine._confidence_score(anomaly),
        }

        return event

    @staticmethod
    def _build_summary(event: Dict[str, Any]) -> str:
        if event.get("anomaly", {}).get("is_anomalous"):
            return (
                f"Suspicious {event.get('event_type')} activity detected "
                f"from {event.get('source_type')} source."
            )
        return "No suspicious activity detected."

    @staticmethod
    def _confidence_score(anomaly: Dict[str, Any]) -> float:
        """
        Confidence is derived from anomaly score
        """
        return round(min(anomaly.get("score", 0.0) + 0.2, 1.0), 2)
