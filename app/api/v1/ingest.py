# app/api/v1/ingest.py

from fastapi import APIRouter, HTTPException
from typing import Dict, Any

from app.core.normalizer import LogNormalizer
from app.core.enricher import LogEnricher
from app.core.anomaly import AnomalyDetector
from app.core.explain import ExplainabilityEngine
from app.core.custody import ChainOfCustody
from app.core.elastic import get_es_client

router = APIRouter(prefix="/ingest", tags=["Ingest"])


@router.post("/")
def ingest_log(payload: Dict[str, Any]):
    """
    Ingest raw log and process through full forensic pipeline.
    """

    try:
        # 1️⃣ Normalize
        event = LogNormalizer.normalize(
            raw_log=payload.get("raw_log", ""),
            source_type=payload.get("source_type", "unknown"),
            device_id=payload.get("device_id", "unknown"),
            user_id=payload.get("user_id", "unknown"),
            event_type=payload.get("event_type", "system"),
            action=payload.get("action", "unknown"),
            severity=payload.get("severity", "low"),
            parsed_fields=payload.get("parsed_fields", {}),
            timestamp=payload.get("timestamp"),
        )

        # 2️⃣ Enrich
        event = LogEnricher.enrich(event)

        # 3️⃣ Anomaly Detection
        event = AnomalyDetector.analyze(event)

        # 4️⃣ Explainability
        event = ExplainabilityEngine.explain(event)

        # 5️⃣ Chain of Custody
        event = ChainOfCustody.generate_hash(event)

        # 6️⃣ Store in Elasticsearch (OPTIONAL during dev)
        try:
            es = get_es_client()
            es.index(index="logs-events", document=event)
        except Exception as es_error:
            # Do NOT crash ingestion if ES is down
            print("Elasticsearch unavailable:", es_error)

        return {
            "status": "success",
            "event_id": event["event_id"],
            "anomalous": event["anomaly"]["is_anomalous"],
            "explanation": event["explanation"],
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
