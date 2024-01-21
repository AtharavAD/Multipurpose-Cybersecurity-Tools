import socket
import tkinter as tk
from tkinter import ttk
from scapy.all import traceroute

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((host, port))
            banner = s.recv(1024).decode('utf-8')
            return True, banner
    except (socket.timeout, ConnectionRefusedError):
        return False, None

def traceroute_analysis(target):
    tracert_result, _ = traceroute(target, maxttl=20)
    return tracert_result

def validate_target(input_target):
    try:
        socket.inet_pton(socket.AF_INET, input_target)
        return True
    except socket.error:
        try:
            socket.gethostbyname(input_target)
            return True
        except socket.error:
            return False

def on_scan_button_click():
    target = target_entry.get()
    if not validate_target(target):
        result_label.config(text="Invalid input. Please enter a valid IP address or domain name.")
        return

    result_text.delete(1.0, tk.END)  # Clear previous results

    common_ports = [21, 22, 25, 53, 80, 110, 143, 443, 445, 3389, 3306, 5432, 123]

    for port in common_ports:
        port_status, banner = scan_port(target, port)
        if port_status:
            result_text.insert(tk.END, f"Port {port} is open. Banner: {banner}\n")
        else:
            result_text.insert(tk.END, f"Port {port} is closed.\n")

    tracert_result = traceroute_analysis(target)
    result_text.insert(tk.END, "\nTraceroute Analysis:\n")
    for hop in tracert_result:
        result_text.insert(tk.END, f"{hop[1].src} ({hop[0].dst})\n")

def on_scan_another_button_click():
    target_entry.delete(0, tk.END)
    result_text.delete(1.0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Foot Printing")
root.iconbitmap("D:\\Multipurpose Cybersecurity Tool\\Favicon\\footprinting.ico")

root.resizable(False, False)

# Calculate the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x_coordinate = (screen_width - 510) // 2
y_coordinate = (screen_height - 430) // 2

# Set the window to be centered on the screen
root.geometry(f"510x430+{x_coordinate}+{y_coordinate}")

# Create and place widgets
target_label = ttk.Label(root, text="Enter a website name or IP address:", font=("Arial", 13))
target_label.place(x=20, y=20)

target_entry = ttk.Entry(root, width=30)
target_entry.place(x=300, y=20)

scan_button = ttk.Button(root, text="Scan", command=on_scan_button_click)
scan_button.place(x=220, y=60)

result_text = tk.Text(root, wrap=tk.WORD, width=58, height=15)
result_text.place(x=20, y=100)

result_label = ttk.Label(root, text="")
result_label.place(x=20, y=100)

scan_another_button = ttk.Button(root, text="Scan Another Target", command=on_scan_another_button_click)
scan_another_button.place(x=200, y=370)

# Start the Tkinter event loop
root.mainloop()
