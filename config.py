# ============================
# Nexify Tools – CONFIG
# ============================

import os

# Paths
DEPOTCACHE = r"C:\Program Files (x86)\Steam\config\depotcache"
STPLUGIN = r"C:\Program Files (x86)\Steam\config\stplug-in"

# UI Style
BRAND_COLOR = "#00a6a9"
BG_COLOR = "#070709"
TEXT_COLOR = "#FFFFFF"

FONT_REGULAR = ("Arial", 11)
FONT_TITLE = ("Arial", 16, "bold")

# Language
LANG = {"current": "cz"}

TEXT = {
    "cz": {
        "title": "Nexify Tools",
        "choose": "Vyber složku nebo ZIP soubor",
        "choose_zip_question": "Chcete vybrat ZIP soubor?\nAno = ZIP soubor, Ne = složka",
        "folder": "Vyber složku nebo ZIP soubor — Nexify Tools",
        "done": "Hotovo!",
        "msg": "Přesunuto: {}\nPřeskočeno: {}\nChyby: {}",
        "steam_not_found": "Steam nebyl nalezen. Kontaktujte podporu na Discordu.",
        "steam_error": "Nepodařilo se spustit Steam.",
        "restart": "Restartovat Steam",
        "restart_done": "Restart Steamu dokončen.",
        "open_logs": "Otevřít logy",
        "support": "Discord podpora"
    },
    "en": {
        "title": "Nexify Tools",
        "choose": "Select a folder or ZIP file",
        "choose_zip_question": "Do you want to select a ZIP file?\nYes = ZIP folder, No = folder",
        "folder": "Select a folder or ZIP file — Nexify Tools",
        "done": "Done!",
        "msg": "Moved: {}\nSkipped: {}\nErrors: {}",
        "steam_not_found": "Steam was not found. Contact support on Discord.",
        "steam_error": "Failed to launch Steam.",
        "restart": "Restart Steam",
        "restart_done": "Steam restart completed.",
        "open_logs": "Open logs",
        "support": "Discord Support"
    }
}

# Logs folder
def logs_folder():
    return os.path.join(os.path.expanduser("~"), "Documents", "NexifyTools", "logs")
