from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess
import sys

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\\Multipurpose Cybersecurity Tool\\UI\\02_Dashboard\\assets\\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.title("Multipurpose cybersecurity Tool")
window.iconbitmap("D:\\Multipurpose Cybersecurity Tool\\Logo.ico")

window.geometry("1080x720")
window.configure(bg = "#FFFFFF")
window.resizable(False, False)

# Calculate the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x_coordinate = (screen_width - 1080) // 2
y_coordinate = (screen_height - 800) // 2

# Set the window to be centered on the screen
window.geometry(f"1080x720+{x_coordinate}+{y_coordinate}")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 720,
    width = 1080,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    93.0,
    25.0,
    anchor="nw",
    text="                 Multipurpose Cybersecurity Tool",
    fill="#000F46",
    font=("Inter Bold", 38 * -1)
)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--Browser_Password_Retrieval--
def open_specific_file1():
    window.after(100, window.destroy)
    file_path = "D:\\Multipurpose Cybersecurity Tool\\UI\\03_tools manual\\Chrome_Password.py"

    try:
        subprocess.Popen(["python", file_path], shell=True)
    except Exception as e:
        print("Error:", e)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_specific_file1,
    relief="flat"
)
button_1.place(
    x=807.0,
    y=558.0,
    width=189.61343383789062,
    height=120.01526641845703
)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--File_Password_Retrieval--
def open_specific_file2():
    window.after(100, window.destroy)
    file_path = "D:\\Multipurpose Cybersecurity Tool\\UI\\03_tools manual\\File_Password_Cracker.py"

    try:
        subprocess.Popen(["python", file_path], shell=True)
    except Exception as e:
        print("Error:", e)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=open_specific_file2,
    relief="flat"
)
button_2.place(
    x=566.0,
    y=558.0,
    width=189.61343383789062,
    height=120.01526641845703
)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--DNS_Enumeration--
def open_specific_file3():
    window.after(100, window.destroy)
    file_path = "D:\\Multipurpose Cybersecurity Tool\\UI\\03_tools manual\\DNS_Enumaration.py"

    try:
        subprocess.Popen(["python", file_path], shell=True)
    except Exception as e:
        print("Error:", e)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=open_specific_file3,
    relief="flat"
)
button_3.place(
    x=325.0,
    y=558.0,
    width=189.61343383789062,
    height=120.01526641845703
)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--SQL_Injection--
def open_specific_file4():
    window.after(100, window.destroy)
    file_path = "D:\\Multipurpose Cybersecurity Tool\\UI\\03_tools manual\\SQL_Injection_Scanner.py"

    try:
        subprocess.Popen(["python", file_path], shell=True)
    except Exception as e:
        print("Error:", e)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=open_specific_file4,
    relief="flat"
)
button_4.place(
    x=84.0,
    y=558.0,
    width=189.61343383789062,
    height=120.01526641845703
)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--Bulk_Extractor--
def open_specific_file5():
    window.after(100, window.destroy)
    file_path = "D:\\Multipurpose Cybersecurity Tool\\UI\\03_tools manual\\Bulk_Extractor.py"

    try:
        subprocess.Popen(["python", file_path], shell=True)
    except Exception as e:
        print("Error:", e)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=open_specific_file5,
    relief="flat"
)
button_5.place(
    x=806.0,
    y=410.0,
    width=189.61343383789062,
    height=120.01526641845703
)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--Mini_DDOS--
def open_specific_file6():
    window.after(100, window.destroy)
    file_path = "D:\\Multipurpose Cybersecurity Tool\\UI\\03_tools manual\\DDOS.py"

    try:
        subprocess.Popen(["python", file_path], shell=True)
    except Exception as e:
        print("Error:", e)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=open_specific_file6,
    relief="flat"
)
button_6.place(
    x=565.0,
    y=410.0,
    width=189.61343383789062,
    height=120.01526641845703
)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--History_Extractor--
def open_specific_file7():
    window.after(100, window.destroy)
    file_path = "D:\\Multipurpose Cybersecurity Tool\\UI\\03_tools manual\\Histexplorer.py"

    try:
        subprocess.Popen(["python", file_path], shell=True)
    except Exception as e:
        print("Error:", e)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=open_specific_file7,
    relief="flat"
)
button_7.place(
    x=324.0,
    y=403.0,
    width=189.61343383789062,
    height=127.01526641845703
)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--Email_Bombing--
def open_specific_file8():
    window.after(100, window.destroy)
    file_path = "D:\\Multipurpose Cybersecurity Tool\\UI\\03_tools manual\\Email_Bombing.py"

    try:
        subprocess.Popen(["python", file_path], shell=True)
    except Exception as e:
        print("Error:", e)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=open_specific_file8,
    relief="flat"
)
button_8.place(
    x=83.0,
    y=410.0,
    width=189.61343383789062,
    height=120.01526641845703
)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--Change_MAC_Address--
def open_specific_file9():
    window.after(100, window.destroy)
    file_path = "D:\\Multipurpose Cybersecurity Tool\\UI\\03_tools manual\\Change_MAc_Address.py"

    try:
        subprocess.Popen(["python", file_path], shell=True)
    except Exception as e:
        print("Error:", e)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=open_specific_file9,
    relief="flat"
)
button_9.place(
    x=806.0,
    y=265.0,
    width=189.61343383789062,
    height=120.01526641845703
)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--WHOIS--
def open_specific_file10():
    window.after(100, window.destroy)
    file_path = "D:\\Multipurpose Cybersecurity Tool\\UI\\03_tools manual\\Whois.py"

    try:
        subprocess.Popen(["python", file_path], shell=True)
    except Exception as e:
        print("Error:", e)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=open_specific_file10,
    relief="flat"
)
button_10.place(
    x=565.0,
    y=265.0,
    width=189.61343383789062,
    height=120.01526641845703
)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-Keylogger--
def open_specific_file11():
    window.after(100, window.destroy)
    file_path = "D:\\Multipurpose Cybersecurity Tool\\UI\\03_tools manual\\Key_Logger.py"

    try:
        subprocess.Popen(["python", file_path], shell=True)
    except Exception as e:
        print("Error:", e)
        
button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=open_specific_file11,
    relief="flat"
)
button_11.place(
    x=324.0,
    y=265.0,
    width=189.61343383789062,
    height=120.01526641845703
)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--Foot_Printing--
def open_specific_file12():
    window.after(100, window.destroy)
    file_path = "D:\\Multipurpose Cybersecurity Tool\\UI\\03_tools manual\\Foot_Printing.py"

    try:
        subprocess.Popen(["python", file_path], shell=True)
    except Exception as e:
        print("Error:", e)
        
button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=open_specific_file12,
    relief="flat"
)
button_12.place(
    x=83.0,
    y=265.0,
    width=189.61343383789062,
    height=120.01526641845703
)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--WiFi_Password_Retrieval--
def open_specific_file13():
    window.after(100, window.destroy)
    file_path = "D:\\Multipurpose Cybersecurity Tool\\UI\\03_tools manual\\Wifi_password.py"

    try:
        subprocess.Popen(["python", file_path], shell=True)
    except Exception as e:
        print("Error:", e)
        
button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=open_specific_file13,
    relief="flat"
)
button_13.place(
    x=807.0,
    y=117.0,
    width=189.61343383789062,
    height=120.01526641845703
)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--Dictionary_Attack--
def open_specific_file14():
    window.after(100, window.destroy)
    file_path = "D:\\Multipurpose Cybersecurity Tool\\UI\\03_tools manual\\Dictionary_Attack.py"

    try:
        subprocess.Popen(["python", file_path], shell=True)
    except Exception as e:
        print("Error:", e)
        
button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=open_specific_file14,
    relief="flat"
)
button_14.place(
    x=566.0,
    y=117.0,
    width=189.61343383789062,
    height=120.01526641845703
)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--Brute_Force_Attack--
def open_specific_file15():
    window.after(100, window.destroy)
    file_path = "D:\\Multipurpose Cybersecurity Tool\\UI\\03_tools manual\\Brute_Force_Attack.py"

    try:
        subprocess.Popen(["python", file_path], shell=True)
    except Exception as e:
        print("Error:", e)
        
button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=open_specific_file15,
    relief="flat"
)
button_15.place(
    x=325.0,
    y=117.0,
    width=189.61343383789062,
    height=120.01526641845703
)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--NMAp--
def open_specific_file16():
    window.after(100, window.destroy)
    file_path = "D:\\Multipurpose Cybersecurity Tool\\UI\\03_tools manual\\NMAP.py"

    try:
        subprocess.Popen(["python", file_path], shell=True)
    except Exception as e:
        print("Error:", e)
        
button_image_16 = PhotoImage(
    file=relative_to_assets("button_16.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=open_specific_file16,
    relief="flat"
)
button_16.place(
    x=84.0,
    y=116.0,
    width=189.61343383789062,
    height=121.01526641845703
)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
window.resizable(False, False)
window.mainloop()
