import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import whois

def perform_whois_lookup(domain):
    try:
        whois_info = whois.whois(domain)
        return whois_info
    except whois.parser.PywhoisError as e:
        return f"Error: {e}"

def on_lookup_button_click():
    domain = domain_entry.get()

    if not domain:
        messagebox.showinfo("Error", "Please enter a domain name.")
        return

    result_text.delete(1.0, tk.END)  # Clear previous results

    # Perform the WHOIS lookup
    result = perform_whois_lookup(domain)

    # Print the WHOIS information or an error message
    if isinstance(result, dict):
        for key, value in result.items():
            result_text.insert(tk.END, f"{key}: {value}\n")
    else:
        result_text.insert(tk.END, result)

    # Enable the "Exit" and "Perform Again" buttons
    exit_button['state'] = 'normal'
    perform_again_button['state'] = 'normal'

def on_exit_button_click():
    root.destroy()

def on_perform_again_button_click():
    # Clear the entry and result text
    domain_entry.delete(0, tk.END)
    result_text.delete(1.0, tk.END)

    # Disable the "Exit" and "Perform Again" buttons
    exit_button['state'] = 'disabled'
    perform_again_button['state'] = 'disabled'

# Create the main window
root = tk.Tk()
root.title("WHOIS Lookup Tool")
root.iconbitmap("D:\\Multipurpose Cybersecurity Tool\\Favicon\\whois.ico")

root.resizable(False, False)

# Calculate the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x_coordinate = (screen_width - 550) // 2
y_coordinate = (screen_height - 430) // 2

# Set the window to be centered on the screen
root.geometry(f"550x430+{x_coordinate}+{y_coordinate}")

# Create and place widgets
title_label = ttk.Label(root)
title_label.grid(row=0, column=0, columnspan=2, pady=10)

domain_label = ttk.Label(root, text="Enter a domain name:", font=("Arial", 13))
domain_label.place(x=20, y=25)

domain_entry = ttk.Entry(root, width=30, font=("Arial", 13))
domain_entry.place(x=210, y=23)

lookup_button = ttk.Button(root, text="Perform WHOIS Lookup", command=on_lookup_button_click)
lookup_button.place(x=200, y=65)

result_text = tk.Text(root, wrap=tk.WORD, width=63, height=15)
result_text.place(x=20, y=110)

exit_button = ttk.Button(root, text="Exit", command=on_exit_button_click, state='disabled')
exit_button.place(x=40, y=370)

perform_again_button = ttk.Button(root, text="Perform Again", command=on_perform_again_button_click, state='disabled')
perform_again_button.place(x=420, y=370)

# Start the Tkinter event loop
root.mainloop()
