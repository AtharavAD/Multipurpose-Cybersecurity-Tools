import tkinter as tk
from tkinter import ttk, filedialog
from pwnedpasswords import Password
from tqdm import tqdm
import pikepdf
import time

def check_password_exposure(password):
    try:
        pwned_password = Password(password)
        return pwned_password.is_pwned
    except Exception as e:
        print(f"Error checking password exposure: {e}")
        return False

def guess_passwords_from_library(pdf_file_path, potential_passwords):
    start_time = time.time()

    for password in tqdm(potential_passwords, "Guessing PDF Password"):
        # Check if the password has been exposed in data breaches
        if check_password_exposure(password):
            continue

        try:
            # Open PDF file and check each password
            with pikepdf.open(pdf_file_path, password=password) as p:
                elapsed_time = time.time() - start_time
                result_label.config(text=f"Password found: {password}\nTime taken: {elapsed_time:.2f} seconds")
                return  # Stop after finding the correct password

        except pikepdf.PasswordError:
            # If password is wrong, continue the loop
            continue

    elapsed_time = time.time() - start_time
    result_label.config(text=f"Password not found in the library.\nTime taken: {elapsed_time:.2f} seconds")

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        pdf_path_var.set(file_path)

def start_password_guessing():
    pdf_file_path = pdf_path_var.get()
    if not pdf_file_path:
        result_label.config(text="Please choose a PDF file.", font=("TkDefaultFont", 12))
        return

    # Load a list of potential passwords from a library (you can customize this list)
    with open("D:\\Multipurpose Cybersecurity Tool\\rockyou.txt", "r", encoding="latin-1") as file:
        potential_passwords = [line.strip() for line in file]

    guess_passwords_from_library(pdf_file_path, potential_passwords)

# Create the main Tkinter window
root = tk.Tk()
root.title("Password Guesser")
root.iconbitmap("D:\\Multipurpose Cybersecurity Tool\\Favicon\\BFA.ico")
root.resizable(False, False)

# Calculate the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x_coordinate = (screen_width - 800) // 2
y_coordinate = (screen_height - 500) // 2

# Set the window to be centered on the screen
root.geometry(f"500x350+{x_coordinate}+{y_coordinate}")

# Create and place widgets in the window
label_file = ttk.Label(root, text="Choose a PDF file:", font=("TkDefaultFont", 12))
label_file.grid(row=0, column=0, padx=10, pady=10)

pdf_path_var = tk.StringVar()
entry_file = ttk.Entry(root, textvariable=pdf_path_var, state="readonly", font=("TkDefaultFont", 12))
entry_file.grid(row=0, column=1, padx=10, pady=10)

button_browse = ttk.Button(root, text="Browse", command=open_file_dialog)
button_browse.grid(row=0, column=2, padx=10, pady=10)

button_start_guessing = ttk.Button(root, text="Start Password Guessing", command=start_password_guessing)
button_start_guessing.grid(row=1, column=0, columnspan=3, pady=10)

result_label = ttk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=1, pady=10)

# Run the Tkinter event loop
root.mainloop()
