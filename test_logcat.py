import subprocess

process = subprocess.Popen(
    ["adb", "logcat", "-v", "time"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    bufsize=0
)

print("Listening to adb logcat...")

for raw_line in iter(process.stdout.readline, b''):
    line = raw_line.decode("utf-8", errors="ignore").strip()
    if line:
        print(line)
