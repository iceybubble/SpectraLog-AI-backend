# app/core/normalizer.py

import uuid
from datetime import datetime
from typing import Dict, Any


class LogNormalizer:
    """
    Converts raw logs from any source into a unified
    forensic-ready SpectraLogAI event format.
    """

    @staticmethod
    def normalize(
        *,
        raw_log: str,
        source_type: str,
        device_id: str = "unknown",
        user_id: str = "unknown",
        event_type: str = "system",
        action: str = "unknown",
        severity: str = "low",
        parsed_fields: Dict[str, Any] | None = None,
        timestamp: str | None = None,
    ) -> Dict[str, Any]:
        """
        Normalize any log into a forensic event.
        """

        return {
            "event_id": str(uuid.uuid4()),

            # Use log timestamp if provided, else ingestion time
            "timestamp": timestamp or datetime.utcnow().isoformat(),

            "source_type": source_type,
            "device_id": device_id,
            "user_id": user_id,

            "event_type": event_type,
            "action": action,
            "severity": severity,

            # Raw evidence (never modified)
            "raw_log": raw_log,

            # Parsed structured fields
            "parsed_fields": parsed_fields or {},

            # Forensic metadata
            "ingested_at": datetime.utcnow().isoformat(),
            "normalized": True,
        }
