import subprocess
import tkinter as tk
from tkinter import scrolledtext

def get_wifi_profiles():
    meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
    data = meta_data.decode("utf-8")
    data = data.split("\n")
    names = []
    for line in data:
        if "All User Profile     : " in line:
            name = line.split(":")[1].strip()
            names.append(name)
    return names

def get_wifi_password(profile_name):
    try:
        meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile_name, 'key=clear'])
        data = meta_data.decode("utf-8", errors="backslashreplace")
        for line in data.split("\n"):
            if "Key Content" in line:
                password = line.split(":")[1].strip()
                return password
    except subprocess.CalledProcessError as e:
        return f"Error retrieving password: {e}"

def show_wifi_profiles():
    output_text.delete(1.0, tk.END)
    for name in get_wifi_profiles():
        password = get_wifi_password(name)
        output_text.insert(tk.END, f"SSID: {name}, Password: {password}\n\n")

# Create the main window
root = tk.Tk()
root.title("Wi-Fi Password Retrieval")
root.iconbitmap("D:\\Multipurpose Cybersecurity Tool\\Favicon\\WIFI pass.ico")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set fixed window size and make it non-resizable
root.resizable(False, False)
x_coordinate = (screen_width - 800) // 2
y_coordinate = (screen_height - 500) // 2
root.geometry(f"700x400+{x_coordinate}+{y_coordinate}")

# Create a button to trigger the Wi-Fi profile retrieval
retrieve_button = tk.Button(root, text="Retrieve Wi-Fi Profiles", command=show_wifi_profiles)
retrieve_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Create a scrolled text widget for displaying the output
output_text = scrolledtext.ScrolledText(root, width=80, height=18, wrap=tk.WORD)
output_text.grid(row=1, column=0, padx=10, pady=10)



# Run the Tkinter event loop
root.mainloop()
