import subprocess
import requests
import re
from datetime import datetime, timezone



INGEST_URL = "http://127.0.0.1:8000/api/v1/ingest/"

LOGCAT_REGEX = re.compile(
    r"(?P<date>\d\d-\d\d)\s+"
    r"(?P<time>\d\d:\d\d:\d\d\.\d+)\s+"
    r"(?P<pid>\d+)\s+"
    r"(?P<tid>\d+)\s+"
    r"(?P<level>[A-Z])\s+"
    r"(?P<tag>[^:]+):\s+"
    r"(?P<message>.*)"
)

def event_type_from_tag(tag: str) -> str:
    tag = tag.lower()
    if "wifi" in tag or "network" in tag:
        return "network"
    if "auth" in tag or "finger" in tag:
        return "auth"
    if "location" in tag or "gps" in tag:
        return "location"
    return "system"

def severity_from_level(level: str) -> str:
    return {"E": "high", "W": "medium"}.get(level, "low")


print("[+] Android logcat collector started")

process = subprocess.Popen(
    ["adb", "logcat"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    bufsize=0
)

sent = 0
unparsed = 0

for raw in iter(process.stdout.readline, b""):
    line = raw.decode("utf-8", errors="ignore").strip()
    if not line:
        continue

    match = LOGCAT_REGEX.match(line)

    if match:
        data = match.groupdict()
        payload = {
            "raw_log": line,
            "source_type": "android",
            "device_id": "android-device-001",
            "event_type": event_type_from_tag(data["tag"]),
            "action": data["tag"],
            "severity": severity_from_level(data["level"]),
            "parsed_fields": {
                "pid": data["pid"],
                "tid": data["tid"],
                "component": data["tag"],
                "message": data["message"],
                "original_timestamp": f"{data['date']} {data['time']}"
            },
            "timestamp": datetime.utcnow().isoformat()
        }
    else:
        # fallback – NEVER DROP REAL LOGS
        payload = {
            "raw_log": line,
            "source_type": "android",
            "device_id": "android-device-001",
            "event_type": "system",
            "action": "unparsed_log",
            "severity": "low",
            "parsed_fields": {},
            "timestamp": datetime.utcnow().isoformat()
        }
        
        unparsed += 1

    try:
        requests.post(INGEST_URL, json=payload, timeout=1)
        sent += 1
        print(f"[SENT] total={sent}, unparsed={unparsed}", end="\r")
    except Exception as e:
        print("\n[ERROR] backend unreachable:", e)
