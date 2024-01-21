import random
import hashlib
import tkinter as tk
from tkinter import messagebox
import time
import math

# Password character set
character = "0123456789abcdefghijklmnopqrstuvwxyz"
character_list = list(character)

# Password strength function
def check_password_strength(password):
    length = len(password)
    has_digit = any(char.isdigit() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_special = any(not char.isalnum() for char in password)

    strength = 0
    if length >= 8:
        strength += 1
    if has_digit:
        strength += 1
    if has_lowercase:
        strength += 1
    if has_uppercase:
        strength += 1
    if has_special:
        strength += 1

    return strength

# Entropy calculation function
def calculate_entropy(password):
    character_set_size = len(set(password))
    entropy = math.log2(character_set_size) * len(password)
    return entropy

# Brute-force password guessing function
def guess_password():
    # Get user's password
    password = entry.get()
    
    # Measure start time
    start_time = time.time()

    # Guess the password
    guess_password = ''
    attempts = 0

    while guess_password != password:
        guess_password = ''.join(random.choices(character_list, k=len(password)))
        attempts += 1

        # Update the GUI with the current attempt
        label_result.config(text=f"   Attempt {attempts}: {guess_password}")
        root.update()

        if guess_password == password:
            end_time = time.time()
            elapsed_time = end_time - start_time
            password_strength = check_password_strength(password)
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            # Calculate password entropy
            entropy = calculate_entropy(password)

            # Display results in the same window with larger font size
            label_result.config(
                text=f"   Your password is: {password}\n"
                f"   Password Strength: {password_strength} out of 5\n"
                f"   Time elapsed: {elapsed_time:.2f} seconds\n"
                f"   SHA-256 Hash of Password: {hashed_password}\n"
                f"   Password Entropy: {entropy:.2f} bits",
                font=("TkDefaultFont", 13),  # Set font size to 5 times bigger
                anchor="w",  # Align text to the left
                justify="left"  # Ensure text is left-justified
            )

            # Provide password complexity suggestions
            if password_strength < 3:
                messagebox.showwarning(
                    "Suggestion",
                    "Consider improving password complexity by adding special characters, numbers, or using a longer password."
                )
            break

# Create the GUI window
root = tk.Tk()
root.title("Brute Force Attack")
root.iconbitmap("D:\\Multipurpose Cybersecurity Tool\\Favicon\\BFA.ico")

# Set fixed window size and make it non-resizable
root.geometry("800x400")
root.resizable(False, False)

# Calculate the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x_coordinate = (screen_width - 800) // 2
y_coordinate = (screen_height - 500) // 2

# Set the window to be centered on the screen
root.geometry(f"800x450+{x_coordinate}+{y_coordinate}")

# Create GUI components
label_prompt = tk.Label(root, text="Enter your password:", anchor="w", font=("Arial", 13))
entry = tk.Entry(root, show="")
button_guess = tk.Button(root, text="Guess Password", command=guess_password, font=("Arial", 13))
label_result = tk.Label(root, text="", anchor="w", font=("Arial", 13), justify="left")

# Spacer label to prevent layout shift
spacer_label = tk.Label(root, text="", width=20)  # Adjust width as needed

# Arrange GUI components
label_prompt.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")
spacer_label.grid(row=0, column=2)  # Spacer label in column 2
button_guess.grid(row=1, column=0, columnspan=2, pady=10)
label_result.grid(row=3, column=0, columnspan=300, pady=10, sticky="w")

# Run the GUI
root.mainloop()
