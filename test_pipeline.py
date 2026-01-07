from app.core.normalizer import LogNormalizer
from app.core.enricher import LogEnricher
from app.core.anomaly import AnomalyDetector

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

# 5️⃣ Print result
import json
print(json.dumps(event, indent=2))
