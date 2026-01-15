import requests, random, time
from datetime import datetime, timezone

URL = "http://localhost:9200/logs-events/_doc"

severities = ["low", "medium", "high", "critical"]
actions = ["app_launch", "network_access", "permission_request", "suspicious_activity"]

for i in range(50):
    now_utc = datetime.now(timezone.utc).isoformat()

    payload = {
        # event time (what happened)
        "@timestamp": now_utc,
        "timestamp": now_utc,

        # ingestion time (when SOC received it)
        "ingested_at": now_utc,

        "event": {
            "category": "android",
            "action": random.choice(actions),
            "severity": random.choice([1, 3, 6, 9])
        },
        "device": {
            "type": "android",
            "id": f"android-device-{random.randint(1,5)}"
        },
        "log": {
            "level": random.choice(severities)
        },
        "source": {
            "ip": f"10.0.0.{random.randint(2,254)}"
        },
        "message": f"simulated android event {i}",
        "data_origin": "synthetic"  
    }

    requests.post(URL, json=payload)
    time.sleep(0.3)

print("Fake Android logs (with ingested_at) sent to logs-events")
