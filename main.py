# ============================
# Nexify Tools – MAIN UI
# ============================

import os
import webbrowser
import tkinter as tk

from config import *
from sorter import sort_files
from steam import restart_steam
from logger import init_log

def open_logs_folder():
    folder = logs_folder()
    os.makedirs(folder, exist_ok=True)
    os.startfile(folder)

def open_support():
    webbrowser.open("https://dsc.gg/steam-zdarma")

def set_lang_ui(code):
    LANG["current"] = code
    label.config(text=TEXT[code]["title"])
    button_sort.config(text=TEXT[code]["choose"])
    restart_button.config(text=TEXT[code]["restart"])
    open_logs_button.config(text=TEXT[code]["open_logs"])
    support_button.config(text=TEXT[code]["support"])

root = tk.Tk()
root.title("Nexify Tools")
root.geometry("420x250")
root.configure(bg=BG_COLOR)

label = tk.Label(root, text=TEXT["cz"]["title"], font=FONT_TITLE, bg=BRAND_COLOR, fg="white")
label.pack(fill="x")

button_sort = tk.Button(root, text=TEXT["cz"]["choose"], command=sort_files,
                        bg=BRAND_COLOR, fg=TEXT_COLOR, font=FONT_REGULAR)
button_sort.pack(pady=6)  # smaller gap

restart_button = tk.Button(root, text=TEXT["cz"]["restart"],
                           command=lambda: restart_steam(init_log()),
                           bg=BRAND_COLOR, fg=TEXT_COLOR, font=FONT_REGULAR)
restart_button.pack(pady=4)

bottom = tk.Frame(root, bg=BG_COLOR)
bottom.pack(side="bottom", fill="x", pady=10)

open_logs_button = tk.Button(bottom, text=TEXT["cz"]["open_logs"],
                             command=open_logs_folder,
                             bg=BRAND_COLOR, fg=TEXT_COLOR, width=15)
open_logs_button.pack(side="left", padx=10)

support_button = tk.Button(bottom, text=TEXT["cz"]["support"],
                           command=open_support,
                           bg=BRAND_COLOR, fg=TEXT_COLOR, width=15)
support_button.pack(side="right", padx=10)

lang_frame = tk.Frame(root, bg=BG_COLOR)
lang_frame.pack()

tk.Button(lang_frame, text="CZ", command=lambda: set_lang_ui("cz"),
          bg=BRAND_COLOR, fg=TEXT_COLOR, width=5).pack(side="left", padx=5)

tk.Button(lang_frame, text="EN", command=lambda: set_lang_ui("en"),
          bg=BRAND_COLOR, fg=TEXT_COLOR, width=5).pack(side="left", padx=5)

root.mainloop()
