# ============================
# Nexify Tools – FILE SORTER
# ============================

import os
import shutil
import zipfile
import tempfile
from tkinter import filedialog, messagebox

from logger import init_log, log_write
from config import TEXT, LANG, DEPOTCACHE, STPLUGIN

def sort_files():
    log_path = init_log()
    log_write(log_path, "sort_files() started.")

    choice = messagebox.askquestion(
        TEXT[LANG["current"]]["title"],
        TEXT[LANG["current"]]["choose_zip_question"]
    )

    temp_dir = None

    if choice == "yes":
        file = filedialog.askopenfilename(
            title=TEXT[LANG["current"]]["folder"],
            filetypes=[("ZIP files", "*.zip")]
        )
        if not file:
            return

        temp_dir = tempfile.mkdtemp()
        with zipfile.ZipFile(file, "r") as z:
            z.extractall(temp_dir)
        folder = temp_dir

    else:
        folder = filedialog.askdirectory(title=TEXT[LANG["current"]]["folder"])
        if not folder:
            return

    moved = []
    skipped = []
    errors = []

    for root, dirs, files in os.walk(folder):
        for fname in files:
            src = os.path.join(root, fname)

            # FILE ASSIGNMENT
            if fname.endswith(".manifest"):
                dest = DEPOTCACHE
            elif fname.endswith(".lua") or fname.endswith(".st") or fname.endswith(".vdf"):
                dest = STPLUGIN
            else:
                skipped.append(src)
                log_write(log_path, f"SKIP: {src}")
                continue

            os.makedirs(dest, exist_ok=True)
            dst = os.path.join(dest, fname)

            try:
                shutil.move(src, dst)
                moved.append(dst)
                log_write(log_path, f"MOVED: {src} → {dst}")
            except Exception as e:
                errors.append(f"{src}: {e}")
                log_write(log_path, f"ERROR moving {src}: {e}")

    if temp_dir:
        shutil.rmtree(temp_dir)

    msg = TEXT[LANG["current"]]["msg"].format(len(moved), len(skipped), len(errors))
    messagebox.showinfo(TEXT[LANG["current"]]["done"], msg)
