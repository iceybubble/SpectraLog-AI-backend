import subprocess

print("Starting adb logcat test...")

process = subprocess.Popen(
    ["adb", "logcat"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    bufsize=0
)

print("Listening to adb output...")

while True:
    raw = process.stdout.readline()
    if not raw:
        continue

    try:
        line = raw.decode("utf-8", errors="ignore").strip()
    except Exception as e:
        print("Decode error:", e)
        continue

    if line:
        print("LOG:", line)
