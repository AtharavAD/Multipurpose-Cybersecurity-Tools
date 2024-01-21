import sqlite3
from datetime import datetime
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def extract_and_display_history(username, limit=50):
    # Construct the path to the Chrome History database based on the provided username
    chrome_history_path = fr'C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\History'

    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(chrome_history_path)
        cursor = connection.cursor()

        # Execute a query to retrieve data from the 'urls' table
        query = f"SELECT url, title, last_visit_time/1000000 as last_visit_time FROM urls ORDER BY last_visit_time DESC LIMIT {limit}"
        cursor.execute(query)

        # Fetch all the results
        results = cursor.fetchall()

        # Create a new folder in the "Documents" directory
        output_folder = fr'C:\Users\{username}\Documents\ChromeHistory'
        os.makedirs(output_folder, exist_ok=True)

        # Display the results
        result_text.delete(1.0, tk.END)  # Clear previous results
        for row in results:
            url, title, last_visit_time = row
            last_visit_time_str = datetime.utcfromtimestamp(last_visit_time).strftime('%Y-%m-%d %H:%M:%S')
            result_text.insert(tk.END, f"URL: {url}\nTitle: {title}\nLast Visit Time: {last_visit_time_str}\n\n")

        # Convert SQLite database to a text file in the new folder
        output_file = os.path.join(output_folder, 'chrome_history.txt')
        with open(output_file, 'w', encoding='utf-8') as file:
            for row in results:
                url, title, last_visit_time = row
                last_visit_time_str = datetime.utcfromtimestamp(last_visit_time).strftime('%Y-%m-%d %H:%M:%S')
                file.write(f"URL: {url}\nTitle: {title}\nLast Visit Time: {last_visit_time_str}\n\n")

        result_text.insert(tk.END, f"\nChrome history extracted and saved to: {output_file}")

    except sqlite3.Error as e:
        result_text.insert(tk.END, f"Error reading SQLite database: {e}")

    finally:
        # Close the database connection
        if connection:
            connection.close()

def browse_folder():
    folder_path = filedialog.askdirectory()
    username_entry.delete(0, tk.END)
    username_entry.insert(tk.END, os.path.basename(folder_path))

def on_extract_button_click():
    username = username_entry.get()
    if not username:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Please enter a Windows username.")
        return

    result_text.delete(1.0, tk.END)  # Clear previous results
    extract_and_display_history(username, limit=50)

# Create the main window
root = tk.Tk()
root.title("History Extractor")
root.resizable(False, False)
root.iconbitmap("D:\\Multipurpose Cybersecurity Tool\\Favicon\\History Explorer.ico")

# Calculate the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x_coordinate = (screen_width - 800) // 2
y_coordinate = (screen_height - 500) // 2

# Set the window to be centered on the screen
root.geometry(f"600x450+{x_coordinate}+{y_coordinate}")

# Create and place widgets
username_label = ttk.Label(root, text="Enter your Windows username:")
username_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

username_entry = ttk.Entry(root, width=30)
username_entry.grid(row=0, column=1, padx=10, pady=5)

browse_button = ttk.Button(root, text="Browse", command=browse_folder)
browse_button.grid(row=0, column=2, padx=10, pady=5)

extract_button = ttk.Button(root, text="Extract History", command=on_extract_button_click)
extract_button.grid(row=1, column=0, columnspan=3, pady=10)

result_text = tk.Text(root, wrap=tk.WORD, width=70, height=20)
result_text.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

# Start the Tkinter event loop
root.mainloop()
