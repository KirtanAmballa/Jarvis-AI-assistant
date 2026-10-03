import os
from datetime import datetime

LOG_FILE = os.path.join("logs", "jarvis_log.txt")


def log_conversation(user, reply):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}]\nUser: {user}\nJarvis: {reply}\n\n")
