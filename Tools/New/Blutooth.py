import tkinter as tk
from tkinter import scrolledtext
import bluetooth

class BluetoothScannerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Bluetooth Scanner")

        self.result_text = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=50, height=15)
        self.result_text.pack()

        self.scan_button = tk.Button(master, text="Scan Bluetooth Devices", command=self.scan_bluetooth_devices)
        self.scan_button.pack()

    def scan_bluetooth_devices(self):
        try:
            # Discover Bluetooth devices with names and classes.
            discovered_devices = bluetooth.discover_devices(lookup_names=True, lookup_class=True)
            # Display information about the scanning process.
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, '[!] Scanning for active devices...\n')
            self.result_text.insert(tk.END, f"[!] Found {len(discovered_devices)} Devices\n\n")
            # Iterate through discovered devices and append their details to the result text.
            for addr, name, device_class in discovered_devices:
                self.result_text.insert(tk.END, f'[+] Name: {name}\n')
                self.result_text.insert(tk.END, f'[+] Address: {addr}\n')
                self.result_text.insert(tk.END, f'[+] Device Class: {device_class}\n\n')
        except Exception as e:
            # Handle and display any exceptions that occur during device discovery
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"[ERROR] An error occurred: {e}")

if __name__ == '__main__':
    root = tk.Tk()
    app = BluetoothScannerGUI(root)
    root.mainloop()
