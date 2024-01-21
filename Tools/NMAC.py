import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess
import winreg
import re

class MacChangerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("MAC Address Changer")
        root.resizable(False, False)

        # Calculate the screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the x and y coordinates to center the window
        x_coordinate = (screen_width - 800) // 2
        y_coordinate = (screen_height - 500) // 2

        # Set the window to be centered on the screen
        root.geometry(f"800x450+{x_coordinate}+{y_coordinate}")
        
        # Initialize variables
        self.mac_to_change_to = ["0A1122334455", "0E1122334455", "021122334455", "061122334455"]
        self.mac_addresses = []
        self.selected_option = tk.StringVar()
        self.update_option = tk.StringVar(value="0")
        
        # Create widgets
        self.label = tk.Label(master, text="Select MAC Address to Change:", font=("Arial", 13), justify="left")
        self.label.place(x=20, y=10)
        
        self.mac_listbox = tk.Listbox(master, selectmode=tk.SINGLE, font=("Arial", 13), width=83, height=2)
        self.mac_listbox.place(x=20, y=45)
        
        self.update_label = tk.Label(master, text="Select New MAC Address:", font=("Arial", 13))
        self.update_label.place(x=20, y=105)
        
        self.update_combobox = ttk.Combobox(master, values=self.mac_to_change_to, textvariable=self.update_option, font=("Arial", 13))
        self.update_combobox.place(x=20, y=140)
        
        self.change_button = tk.Button(master, text="Change MAC Address", command=self.change_mac_address, font=("Arial", 10))
        self.change_button.place(x=20, y=190)
        
    def get_mac_addresses(self):
        getmac_output = subprocess.run("getmac", capture_output=True).stdout.decode().split('\n')
        for macAdd in getmac_output:
            macFind = macAddRegex.search(macAdd)
            transportFind = transportName.search(macAdd)
            if macFind and transportFind:
                self.mac_addresses.append((macFind.group(0), transportFind.group(0)))
        
    def populate_mac_listbox(self):
        self.get_mac_addresses()
        for index, item in enumerate(self.mac_addresses):
            self.mac_listbox.insert(index, f"Mac Address: {item[0]} - Transport Name: {item[1]}")
        
    def change_mac_address(self):
        selected_index = self.mac_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a MAC address.")
            return

        option = int(selected_index[0])
        update_option = self.update_option.get()

        try:
            controller_key_part = r"SYSTEM\ControlSet001\Control\Class\{4d36e972-e325-11ce-bfc1-08002be10318}"
            with winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE) as hkey:
                controller_key_folders = [("\\000" + str(item) if item < 10 else "\\00" + str(item)) for item in range(0, 21)]
                for key_folder in controller_key_folders:
                    try:
                        with winreg.OpenKey(hkey, controller_key_part + key_folder, 0, winreg.KEY_ALL_ACCESS) as regkey:
                            try:
                                count = 0
                                while True:
                                    name, value, type = winreg.EnumValue(regkey, count)
                                    count = count + 1
                                    if name == "NetCfgInstanceId" and value == self.mac_addresses[option][1]:
                                        new_mac_address = self.mac_to_change_to[update_option]
                                        winreg.SetValueEx(regkey, "NetworkAddress", 0, winreg.REG_SZ, new_mac_address)
                                        messagebox.showinfo("Success", "MAC address changed successfully.")
                                        break
                            except WindowsError:
                                pass
                    except:
                        pass

            run_disable_enable = messagebox.askyesno("Confirmation", "Do you want to disable and reenable your wireless device(s)?")
            if run_disable_enable:
                self.disable_enable_network_adapters()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def disable_enable_network_adapters(self):
        try:
            network_adapters = subprocess.run(["wmic", "nic", "get", "name,index"], capture_output=True).stdout.decode('utf-8', errors="ignore").split('\r\r\n')
            for adapter in network_adapters:
                adapter_index_find = adapterIndex.search(adapter.lstrip())
                if adapter_index_find and "Wireless" in adapter:
                    disable = subprocess.run(["wmic", "path", "win32_networkadapter", "where", f"index={adapter_index_find.group(0)}", "call", "disable"], capture_output=True)
                    if disable.returncode == 0:
                        print(f"Disabled {adapter.lstrip()}")
                    enable = subprocess.run(["wmic", "path", "win32_networkadapter", "where", f"index={adapter_index_find.group(0)}", "call", "enable"], capture_output=True)
                    if enable.returncode == 0:
                        print(f"Enabled {adapter.lstrip()}")

            getmac_output = subprocess.run("getmac", capture_output=True).stdout.decode()
            new_mac_address = self.mac_to_change_to[int(self.update_option.get())]
            transport_name_to_match = self.mac_addresses[int(self.selected_option.get())][1]
            if new_mac_address in getmac_output and transport_name_to_match in getmac_output:
                print("Mac Address Success")


        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during disable/enable: {e}")

if __name__ == "__main__":
    macAddRegex = re.compile(r"([A-Za-z0-9]{2}[:-]){5}([A-Za-z0-9]{2})")
    transportName = re.compile("({.+})")
    adapterIndex = re.compile("([0-9]+)")

    root = tk.Tk()
    app = MacChangerGUI(root)
    app.populate_mac_listbox()
    root.mainloop()
