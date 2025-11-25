# ============================
# Nexify Tools – STEAM
# ============================

import os
import time
import subprocess
import psutil
from tkinter import messagebox
from logger import log_write
from config import TEXT, LANG

def find_steam():
    drives = ["C","D","E","F","G","H"]
    paths = []

    for d in drives:
        paths += [
            fr"{d}:\Program Files (x86)\Steam\Steam.exe",
            fr"{d}:\Program Files\Steam\Steam.exe"
        ]

    for p in paths:
        if os.path.exists(p):
            return p

    return None


def restart_steam(log_path):
    log_write(log_path, "Restarting Steam...")

    for proc in psutil.process_iter(["name", "pid"]):
        if "steam" in (proc.info["name"] or "").lower():
            try:
                proc.terminate()
                proc.wait(5)
                log_write(log_path, f"Terminated Steam PID: {proc.pid}")
            except:
                try:
                    proc.kill()
                    log_write(log_path, f"Killed Steam PID: {proc.pid}")
                except:
                    log_write(log_path, f"Failed to kill Steam PID: {proc.pid}")

    time.sleep(2)

    steam_path = find_steam()
    if not steam_path:
        messagebox.showerror("Error", TEXT[LANG["current"]]["steam_not_found"])
        log_write(log_path, "ERROR: Steam not found.")
        return

    try:
        subprocess.Popen([steam_path], close_fds=True)
        log_write(log_path, f"Steam started: {steam_path}")
    except Exception as e:
        log_write(log_path, f"ERROR starting Steam: {e}")
        messagebox.showerror("Error", TEXT[LANG["current"]]["steam_error"])
        return

    messagebox.showinfo("OK", TEXT[LANG["current"]]["restart_done"])
