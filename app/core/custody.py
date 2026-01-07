# app/core/custody.py

import hashlib
import json
from datetime import datetime
from typing import Dict, Any


class ChainOfCustody:
    """
    Ensures forensic integrity of logs and evidence
    using cryptographic hashing.
    """

    HASH_ALGORITHM = "sha256"

    @staticmethod
    def generate_hash(event: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate and attach evidence hash to an event.
        """

        # Create a stable copy of event (exclude volatile fields)
        stable_event = {
            k: v for k, v in event.items()
            if k not in {"ingested_at", "evidence", "custody"}
        }

        serialized = json.dumps(
            stable_event,
            sort_keys=True,
            separators=(",", ":")
        ).encode("utf-8")

        hash_value = hashlib.sha256(serialized).hexdigest()

        event["custody"] = {
            "evidence_hash": hash_value,
            "hash_algorithm": ChainOfCustody.HASH_ALGORITHM,
            "generated_at": datetime.utcnow().isoformat(),
        }

        return event

    @staticmethod
    def verify_integrity(event: Dict[str, Any]) -> bool:
        """
        Verify event integrity using stored hash.
        """

        custody = event.get("custody")
        if not custody:
            return False

        original_hash = custody.get("evidence_hash")

        stable_event = {
            k: v for k, v in event.items()
            if k not in {"ingested_at", "custody"}
        }

        serialized = json.dumps(
            stable_event,
            sort_keys=True,
            separators=(",", ":")
        ).encode("utf-8")

        recalculated_hash = hashlib.sha256(serialized).hexdigest()

        return recalculated_hash == original_hash
