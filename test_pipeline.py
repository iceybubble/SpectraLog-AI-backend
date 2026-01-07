from app.core.normalizer import LogNormalizer
from app.core.enricher import LogEnricher
from app.core.anomaly import AnomalyDetector
from app.core.explain import ExplainabilityEngine
from app.core.custody import ChainOfCustody



# 1️⃣ Simulate a raw log (Android example)
raw_log = "Failed login attempt from 8.8.8.8 at 02:30"

# 2️⃣ Normalize
event = LogNormalizer.normalize(
    raw_log=raw_log,
    source_type="android",
    device_id="pixel-7",
    user_id="user_123",
    event_type="auth",
    action="login_failed",
    severity="high",
    parsed_fields={
        "ip": "8.8.8.8"
    }
)

# 3️⃣ Enrich
event = LogEnricher.enrich(event)

# 4️⃣ Analyze for anomaly
event = AnomalyDetector.analyze(event)

event = ExplainabilityEngine.explain(event)

event = ChainOfCustody.generate_hash(event)

# 5️⃣ Print result

import json
print(json.dumps(event["explanation"], indent=2))

print("Evidence hash:", event["custody"]["evidence_hash"])

is_valid = ChainOfCustody.verify_integrity(event)
print("Integrity valid?", is_valid)

event["severity"] = "low"
ChainOfCustody.verify_integrity(event)