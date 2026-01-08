import requests, random, time
from datetime import datetime, timezone

URL = "http://localhost:9200/spectralog-test/_doc"

severities = ["low", "medium", "high", "critical"]

for i in range(50):
    payload = {
        "@timestamp": datetime.now(timezone.utc).isoformat(),
        "severity": random.choice(severities),
        "device_type": "android",
        "device_id": f"android-device-{random.randint(1,5)}",
        "message": f"simulated android event {i}"
    }

    requests.post(URL, json=payload)
    time.sleep(0.3)

print("Log burst simulation completed")
