import os
import time
import psutil
import requests
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
CPU_THRESHOLD = int(os.getenv("CPU_THRESHOLD", 80))
DISK_THRESHOLD = int(os.getenv("DISK_THRESHOLD", 90))
MEMORY_THRESHOLD = int(os.getenv("MEMORY_THRESHOLD", 80))

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, json=data)
    except Exception as e:
        print(f"Failed to send Telegram message: {e}")

def monitor_system():
    while True:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        alert_msgs = []

        if cpu > CPU_THRESHOLD:
            alert_msgs.append(f"⚠️ *High CPU Usage:* {cpu}%")
        if memory > MEMORY_THRESHOLD:
            alert_msgs.append(f"⚠️ *High Memory Usage:* {memory}%")
        if disk > DISK_THRESHOLD:
            alert_msgs.append(f"⚠️ *High Disk Usage:* {disk}%")

        if alert_msgs:
            send_telegram_message("\n".join(alert_msgs))
        else:
            status_msg = f"✅ System OK\nCPU: {cpu}%\nMemory: {memory}%\nDisk: {disk}%"
            send_telegram_message(status_msg)

        time.sleep(300)  # wait 5 minutes

if __name__ == "__main__":
    monitor_system()