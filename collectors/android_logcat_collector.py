import subprocess
import requests
import json
import datetime

API_URL = "http://localhost:8000/api/v1/ingest"

def stream_logcat():
    # Start adb logcat process
    process = subprocess.Popen(
        ["adb", "logcat", "-v", "time"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )

    print(" Streaming Android logcat... (Ctrl+C to stop)")

    for line in process.stdout:
        line = line.strip()
        if not line:
            continue

        payload = {
            "device_type": "android",
            "device_id": "MY_ANDROID",
            "event_type": "android_logcat",
            "message": line,
            "severity": "info",
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "details": {}
        }

        try:
            response = requests.post(API_URL, json=payload)
            if response.status_code != 200:
                print(" Failed to send:", response.text)
            else:
                print(" Sent:", line)
        except Exception as e:
            print("ERROR:", e)

if __name__ == "__main__":
    stream_logcat()
