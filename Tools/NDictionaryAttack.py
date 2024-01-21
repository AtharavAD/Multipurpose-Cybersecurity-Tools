import tkinter as tk
from tkinter import messagebox
import pwnedpasswords
import time
import hashlib
import string
import random
import math

def check_password_strength():
    password = password_entry.get().strip()  # Remove leading and trailing whitespaces
    if not password:
        messagebox.showwarning("Warning", "Please enter a password before checking.")
        return

    start_time = time.time()
    result = pwnedpasswords.check(password)
    end_time = time.time()
    time_taken = end_time - start_time

    result_text.set(f"Typed Password: {password}")

    if result == 0:
        result_text.set(result_text.get() + "\nPassword is strong and not found in common password lists.")
    else:
        result_text.set(result_text.get() + f"\nPassword is weak and appears in {result} common password lists.")
        result_text.set(result_text.get() + f"\nTime taken to guess: {time_taken:.2f} seconds")

    # SHA-256 hash of the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    result_text.set(result_text.get() + f"\nSHA-256 Hash of Password: {hashed_password}")

    # Password entropy calculation
    entropy = calculate_entropy(password)
    result_text.set(result_text.get() + f"\nPassword Entropy: {entropy:.2f} bits")

def calculate_entropy(password):
    character_set_size = len(set(password))
    entropy = math.log2(character_set_size) * len(password)
    return entropy

def on_exit():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Dictionary Attack")
root.iconbitmap("D:\\Multipurpose Cybersecurity Tool\\Favicon\\Dictionary Attack.ico")

# Set fixed window size and make it non-resizable
root.geometry("800x450")
root.resizable(False, False)

# Calculate the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x_coordinate = (screen_width - 800) // 2
y_coordinate = (screen_height - 500) // 2

# Set the window to be centered on the screen
root.geometry(f"800x450+{x_coordinate}+{y_coordinate}")

# Create and place widgets
password_label = tk.Label(root, text="Enter a password to check:", font=("TkDefaultFont", 13))
password_label.grid(row=0, column=0, pady=10, padx=10, sticky='w')

password_entry = tk.Entry(root, show="*", font=("TkDefaultFont", 13))
password_entry.grid(row=0, column=1, pady=10, padx=10)

check_button = tk.Button(root, text="Check Password", command=check_password_strength, font=("TkDefaultFont", 13))
check_button.grid(row=2, columnspan=15, pady=20, padx=0)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("TkDefaultFont", 13), justify="left")
result_label.grid(row=3, columnspan=300, pady=10, padx=10)

# Run the Tkinter event loop
root.mainloop()
