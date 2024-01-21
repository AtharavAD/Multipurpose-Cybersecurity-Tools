import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def copy_folder():
    source_folder = source_entry.get()
    destination_folder = destination_entry.get()

    # Check if source and destination are selected
    if not source_folder or not destination_folder:
        messagebox.showerror("Error", "Please select both source and destination folders.")
        return

    try:
        # Create the destination folder if it doesn't exist
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Copy the contents of the source folder to the destination folder
        shutil.copytree(source_folder, os.path.join(destination_folder, "extracted_files"))

        # Create a report file in the copied folder
        report_file_path = os.path.join(destination_folder, "extracted_files", "report.txt")
        with open(report_file_path, 'w') as report_file:
            report_file.write(f"Report for copied folder:\n\n")
            for root, dirs, files in os.walk(os.path.join(destination_folder, "extracted_files")):
                report_file.write(f"Directory: {root}\n")
                for file in files:
                    report_file.write(f"  - {file}\n")

        result_label.config(text=f"Folder '{source_folder}' copied to '{destination_folder}/extracted_files'.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def open_destination_folder():
    destination_folder = destination_entry.get()
    os.startfile(os.path.join(destination_folder, "extracted_files"))

# Create the main window
root = tk.Tk()
root.title("Mini Extractor")
root.iconbitmap("D:\\Multipurpose Cybersecurity Tool\\Favicon\\Bulk Extractor.ico")

root.geometry("600x250")  # Set a fixed size for the window
root.resizable(False, False)

# Calculate the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x_coordinate = (screen_width - 600) // 2
y_coordinate = (screen_height - 500) // 2

# Set the window to be centered on the screen
root.geometry(f"600x250+{x_coordinate}+{y_coordinate}")

# Create and place widgets
source_label = tk.Label(root, text="Source Folder:", font=("TkDefaultFont", 13))
source_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

source_entry = tk.Entry(root, width=50)
source_entry.grid(row=1, column=1, padx=10, pady=10)

browse_source_button = tk.Button(root, text="Browse", command=lambda: source_entry.insert(tk.END, filedialog.askdirectory()), font=("TkDefaultFont", 10))
browse_source_button.grid(row=1, column=2, padx=10, pady=10)

destination_label = tk.Label(root, text="Destination Folder:", font=("TkDefaultFont", 13))
destination_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

destination_entry = tk.Entry(root, width=50)
destination_entry.grid(row=2, column=1, padx=10, pady=10)

browse_destination_button = tk.Button(root, text="Browse", command=lambda: destination_entry.insert(tk.END, filedialog.askdirectory()), font=("TkDefaultFont", 10))
browse_destination_button.grid(row=2, column=2, padx=10, pady=10)

copy_button = tk.Button(root, text="Copy Folder", command=copy_folder, font=("TkDefaultFont", 10))
copy_button.grid(row=3, column=0, columnspan=3, pady=20)

open_folder_button = tk.Button(root, text="Open Extracted Folder", command=open_destination_folder, font=("TkDefaultFont", 10))
open_folder_button.grid(row=5, column=0, columnspan=3, pady=10)

result_label = tk.Label(root, text="", font=("TkDefaultFont", 10))
result_label.grid(row=4, column=0, columnspan=3)

# Start the Tkinter event loop
root.mainloop()
