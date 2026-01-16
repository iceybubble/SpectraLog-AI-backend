import time
import smtplib
from email.mime.text import MIMEText
from elasticsearch import Elasticsearch

# Elasticsearch connection
ELASTIC_URL = "http://localhost:9200"
ALERT_INDEX = "soc-alerts"

# Email settings
EMAIL_FROM = "meakru40@gmail.com"     # sender (can be same as receiver)
EMAIL_TO = "meakru40@gmail.com"       # receiver
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_PASSWORD = "oocg gkdm ifmj edew"

# How often to check for new alerts (seconds)
CHECK_INTERVAL = 60


es = Elasticsearch(ELASTIC_URL)

# This set keeps track of alerts already emailed
sent_alert_ids = set()

print("[+] SOC Email Notifier started...")
print("[+] Watching index:", ALERT_INDEX)


def send_email(subject, body):
    msg = MIMEText(body)
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg["Subject"] = subject

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()  # encrypt connection
        server.login(EMAIL_FROM, SMTP_PASSWORD)
        server.send_message(msg)


while True:
    try:
        # Get latest alerts from soc-alerts
        response = es.search(
            index=ALERT_INDEX,
            size=10,
            sort="@timestamp:desc"
        )

        for hit in response["hits"]["hits"]:
            alert_id = hit["_id"]

            # Skip alerts already emailed
            if alert_id in sent_alert_ids:
                continue

            alert = hit["_source"]

            rule_name = alert.get("rule_name", "Unknown Rule")
            timestamp = alert.get("@timestamp", "N/A")
            action_group = alert.get("action_group", "N/A")

            subject = f"[SOC ALERT] {rule_name}"
            body = f"""
 SOC ALERT DETECTED 

Rule Name   : {rule_name}
Action Group: {action_group}
Time        : {timestamp}

Check Kibana → soc-alerts for investigation.
"""

            send_email(subject, body)
            sent_alert_ids.add(alert_id)

            print(f"[+] Email sent for alert: {rule_name}")

    except Exception as e:
        print("[!] Error:", e)

    time.sleep(CHECK_INTERVAL)
