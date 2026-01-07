import subprocess
import sys

print(">>> Script started", flush=True)

process = subprocess.Popen(
    ["adb", "logcat"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    bufsize=0
)

print(">>> adb logcat started", flush=True)

count = 0

while True:
    raw = process.stdout.readline()
    if not raw:
        continue

    line = raw.decode("utf-8", errors="ignore").strip()
    if not line:
        continue

    count += 1
    print(f"[{count}] {line}", flush=True)
