# Telegram-Integrated System Monitor on AWS EC2

This project sets up a lightweight system monitoring solution that sends real-time system metrics and alerts to a Telegram chat from an EC2 instance.

## Features

- Sends CPU, memory, and disk usage metrics at regular intervals
- Alerts when thresholds are breached (high CPU, low disk space, etc.)
- Configurable schedule and thresholds

## Requirements

- Python 3.x
- AWS EC2 instance (Ubuntu recommended)
- Telegram Bot Token and Chat ID

## Setup

1. Clone the repo and SSH into your EC2 instance.
2. Run `pip install -r requirements.txt`.
3. Set environment variables in `.env`.
4. Run the script with: `python monitor.py &`

## Environment Variables

Create a `.env` file with the following content:

```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
CPU_THRESHOLD=80
DISK_THRESHOLD=90
MEMORY_THRESHOLD=80
```

## Automate at Boot

Add the script to crontab for persistent monitoring:

```bash
@reboot /usr/bin/python3 /home/ubuntu/telegram_system_monitor_ec2/monitor.py
```# telegram_monitor_ec2
