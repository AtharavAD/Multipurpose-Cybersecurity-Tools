import sqlite3
from datetime import datetime
import os
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog

class ChromeHistoryExtractorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Chrome History Extractor")
        self.master.geometry("600x400")

        self.label_username = ttk.Label(master, text="Enter your Windows username:")
        self.label_username.pack(pady=10)

        self.entry_username = ttk.Entry(master)
        self.entry_username.pack(pady=10)

        self.button_extract = ttk.Button(master, text="Extract Chrome History", command=self.extract_and_display_history)
        self.button_extract.pack(pady=20)

        self.text_display = scrolledtext.ScrolledText(master, width=70, height=15, wrap=tk.WORD)
        self.text_display.pack(padx=10, pady=10)

    def extract_and_display_history(self):
        username = self.entry_username.get()

        if not username:
            messagebox.showerror("Error", "Please enter a valid Windows username.")
            return

        try:
            history_text = self.extract_history(username, limit=50)
            self.text_display.delete(1.0, tk.END)
            self.text_display.insert(tk.END, history_text)
            messagebox.showinfo("Extraction Complete", "Chrome history extracted successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def extract_history(self, username, limit=50):
        chrome_history_path = fr'C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\History'
        connection = sqlite3.connect(chrome_history_path)
        cursor = connection.cursor()

        query = f"SELECT url, title, last_visit_time/1000000 as last_visit_time FROM urls ORDER BY last_visit_time DESC LIMIT {limit}"
        cursor.execute(query)
        results = cursor.fetchall()

        history_text = ""
        for row in results:
            url, title, last_visit_time = row
            last_visit_time_str = datetime.utcfromtimestamp(last_visit_time).strftime('%Y-%m-%d %H:%M:%S')
            history_text += f"URL: {url}\nTitle: {title}\nLast Visit Time: {last_visit_time_str}\n\n"

        connection.close()
        return history_text

def save_to_file(text):
    file_path = tk.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)
        messagebox.showinfo("File Saved", f"History saved to: {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChromeHistoryExtractorGUI(root)
    save_button = ttk.Button(root, text="Save History to File", command=lambda: save_to_file(app.text_display.get(1.0, tk.END)))
    save_button.pack(pady=10)
    root.mainloop()
