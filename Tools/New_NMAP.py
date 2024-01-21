import tkinter as tk
from tkinter import messagebox
import nmap
import re

# Define regular expressions and global variables
ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
port_min = 0
port_max = 65535
open_ports = []
ip_address = None  # Initialize ip_address to None

def scan_ports():
    global ip_address, port_min, port_max
    try:
        nm = nmap.PortScanner()
        for port in range(port_min, port_max + 1):
            result = nm.scan(ip_address, str(port))
            port_status = result['scan'][ip_address]['tcp'][port]['state']
            output_text.insert(tk.END, f"Port {port} is {port_status}\n")
    except Exception as e:
        output_text.insert(tk.END, f"Error: {e}\n")

def start_scan():
    global ip_address, port_min, port_max, ip_add_pattern, port_range_pattern
    ip_address = ip_entry.get()
    port_range = port_entry.get()
    
    if not ip_add_pattern.search(ip_address):
        messagebox.showerror("Error", "Invalid IP address")
        return

    port_range_valid = port_range_pattern.search(port_range.replace(" ", ""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
    else:
        messagebox.showerror("Error", "Invalid port range")
        return

    output_text.delete(1.0, tk.END)  # Clear previous output
    scan_ports()

# Create main window
window = tk.Tk()
window.title("NMAP Port Scanner")
window.iconbitmap("D:\\Multipurpose Cybersecurity Tool\\Favicon\\NMAP.ico")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set fixed window size and make it non-resizable
window.resizable(False, False)
x_coordinate = (screen_width - 500) // 2
y_coordinate = (screen_height - 400) // 2
window.geometry(f"480x400+{x_coordinate}+{y_coordinate}")

# IP Entry
ip_label = tk.Label(window, text="Enter IP address:", justify="left", font=("Arial", 13))
ip_label.pack()
ip_label.place(x=15,y=20)

ip_entry = tk.Entry(window)
ip_entry.pack()
ip_entry.place(x=155, y=21)

# Port Entry
port_label = tk.Label(window, text="Enter port range (e.g., 60-120):", font=("Arial", 13))
port_label.pack()
port_label.place(x=15, y=60)

port_entry = tk.Entry(window)
port_entry.pack()
port_entry.place(x=255, y=62)

# Start Scan Button
scan_button = tk.Button(window, text="Start Scan", command=start_scan, font=("Arial", 10))
scan_button.pack()
scan_button.place(x=200, y=110)

# Output Text
output_text = tk.Text(window, height=12, width=55)
output_text.pack()
output_text.place(x=15, y=155)

# Run Tkinter event loop
window.mainloop()
