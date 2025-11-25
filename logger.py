# ============================
# Nexify Tools – LOGGER
# ============================

import os
from datetime import datetime
from config import logs_folder

def init_log():
    folder = logs_folder()
    os.makedirs(folder, exist_ok=True)

    path = os.path.join(folder, f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt")

    with open(path, "w", encoding="utf-8") as f:
        f.write("Nexify Tools Log\n")
        f.write(f"Started: {datetime.now()}\n\n")

    return path

def log_write(path, msg):
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}\n")
