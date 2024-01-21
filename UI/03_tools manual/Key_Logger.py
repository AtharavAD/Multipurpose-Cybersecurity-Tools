import tkinter as tk
from tkinter import PhotoImage
import subprocess
import time

window = tk.Tk()
window.geometry("1080x720")
window.title("Multipurpose Cybersecurity tool")

window.resizable(False, False)
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width - 1080) // 2
y_coordinate = (screen_height - 800) // 2
window.geometry(f"1080x720+{x_coordinate}+{y_coordinate}")

label = tk.Label(window, text="           KEYLOGGER", font=('Inter', 30, 'bold'), fg='#000f46')
label.place(x=300, y=30)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Introduction_page():
    Introduction_frame = tk.Frame(main_frame)
    lb = tk.Label(Introduction_frame, text=Introduction_text, font=('Inter',15), fg='#000f46', bg='#e5e5e5', justify='left')
    lb.pack()
    Introduction_frame.pack(pady=20)
    Introduction_frame.place(x=15, y=15)

def Steps_page():
    Steps_frame = tk.Frame(main_frame)
    lb = tk.Label(Steps_frame, text=Steps_text, font=('Inter',15), fg='#000f46', bg='#e5e5e5', justify='left')
    lb.pack()
    Steps_frame.pack(pady=20)
    Steps_frame.place(x=15, y=15)

def Insights_page():
    Insights_frame = tk.Frame(main_frame)
    lb1 = tk.Label(Insights_frame, text=Insights_text,font=('Inter',15), fg='#000f46', bg='#e5e5e5', justify='left')
    lb1.pack()
    Insights_frame.pack(pady=20)
    Insights_frame.place(x=15, y=15)

def Application_page():
    Application_frame = tk.Frame(main_frame)
    lb = tk.Label(Application_frame, text=Application_text, font=('Inter',15), fg='#000f46', bg='#e5e5e5', justify='left')
    lb.pack()
    Application_frame.pack(pady=20)
    Application_frame.place(x=15, y=15)

def Results_page():
    Results_frame = tk.Frame(main_frame)
    lb = tk.Label(Results_frame, image=Result, font=('Inter',15), fg='#000f46', bg='#e5e5e5')
    lb.pack()
    Results_frame.pack(pady=20)
    Results_frame.place(x=15, y=15)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def hide_indicators():
    Introduction_indicate.config(bg='#e5e5e5')
    Steps_indicate.config(bg='#e5e5e5')
    Insights_indicate.config(bg='#e5e5e5')
    Application_indicate.config(bg='#e5e5e5')
    Results_indicate.config(bg='#e5e5e5')

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def indicate(lb, page):
    hide_indicators()
    lb.config(bg='#000f46')
    delete_pages()
    page()

options_frame = tk.Frame(window, bg='#e5e5e5')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Introduction_btn = tk.Button(options_frame, text='Introduction',
                             font=('Inter',20,'bold'), fg='#000f46', bd=0, bg='#e5e5e5',
                             command=lambda: indicate(Introduction_indicate, Introduction_page))
Introduction_btn.place(x=30, y=20)

Introduction_indicate = tk.Label(options_frame, text='', bg='#e5e5e5')
Introduction_indicate.place(x=20, y=25, width=4, height=35)


Steps_btn = tk.Button(options_frame, text='Steps',
                             font=('Inter',20,'bold'), fg='#000f46', bd=0, bg='#e5e5e5',
                             command=lambda: indicate(Steps_indicate, Steps_page))
Steps_btn.place(x=30, y=75)

Steps_indicate = tk.Label(options_frame, text='', bg='#e5e5e5')
Steps_indicate.place(x=20, y=80, width=4, height=35)


Insights_btn = tk.Button(options_frame, text='Insights',
                             font=('Inter',20,'bold'), fg='#000f46', bd=0, bg='#e5e5e5',
                             command=lambda: indicate(Insights_indicate, Insights_page))
Insights_btn.place(x=30, y=130)

Insights_indicate = tk.Label(options_frame, text='', bg='#e5e5e5')
Insights_indicate.place(x=20, y=135, width=4, height=35)


Application_btn = tk.Button(options_frame, text='Applications',
                             font=('Inter',20,'bold'), fg='#000f46', bd=0, bg='#e5e5e5',
                             command=lambda: indicate(Application_indicate, Application_page))
Application_btn.place(x=30, y=185)

Application_indicate = tk.Label(options_frame, text='', bg='#e5e5e5')
Application_indicate.place(x=20, y=190, width=4, height=35)


Results_btn = tk.Button(options_frame, text='Results',
                             font=('Inter',20,'bold'), fg='#000f46', bd=0, bg='#e5e5e5',
                             command=lambda: indicate(Results_indicate, Results_page))
Results_btn.place(x=30, y=240)

Results_indicate = tk.Label(options_frame, text='', bg='#e5e5e5')
Results_indicate.place(x=20, y=245, width=4, height=35)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
options_frame.pack()
options_frame.pack_propagate(False)
options_frame.configure(width=255, height=575)
options_frame.place(x=30, y=115)


main_frame = tk.Frame(window, bg='#e5e5e5')

main_frame.pack()
main_frame.pack_propagate(False)
main_frame.configure(width=747, height=575)
main_frame.place(x=303, y=115)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def open_specific_file1():

    window.after(100, window.destroy)
    
    # Specify the path to the Python script you want to open
    file_path = "D:\\Multipurpose Cybersecurity Tool\\UI\\02_Dashboard\\gui.py"

    # Use subprocess to execute the Python script
    try:
        subprocess.Popen(["python", file_path], shell=True)
    except Exception as e:
        print("Error:", e)

image1 = PhotoImage(file="D:\\Multipurpose Cybersecurity Tool\\UI\\back4.png")
back_btn = tk.Button(window, image=image1,
                             font=('Inter',20,'bold'), fg='#000f46', bd=0,
                             command=open_specific_file1)
back_btn.place(x=35, y=35)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def open_popup():
    popup = tk.Toplevel(window)
    popup.title("Popup Window")
    
    label = tk.Label(popup, text="This is a popup window.")
    label.pack(padx=20, pady=10)

    ok_button = tk.Button(popup, text="OK", command=popup.destroy)
    ok_button.pack(pady=10)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def open_specific_file2():
    
    # Specify the path to the Python script you want to open
    file_path = "D:\\Multipurpose Cybersecurity Tool\\Tools\\Keylogger.py"

    # Use subprocess to execute the Python script
    try:
        subprocess.Popen(["python", file_path], shell=True)
    except Exception as e:
        print("Error:", e)

image2 = PhotoImage(file="D:\\Multipurpose Cybersecurity Tool\\UI\\play.png")
back_btn = tk.Button(window, image=image2,
                             font=('Inter',20,'bold'), fg='#000f46', bd=0,
                             command=open_specific_file2)
back_btn.place(x=1000, y=35)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Introduction_text = """
A keylogger, short for "keystroke logger," is a type of software or hardware device 
designed to record a user's keystrokes on a computer or mobile device without 
their knowledge or consent. Keyloggers can be used for various purposes, both 
legitimate and malicious.

Types of Keyloggers:

1. Software Keyloggers: These are programs installed on a computer system or 
    mobile device. They can be spread through malicious email attachments, 
    infected software downloads, or compromised websites.

2. Hardware Keyloggers: These are physical devices connected between the 
    computer's keyboard and the computer itself. They record keystrokes onto 
    their internal memory and are retrieved later to access the recorded data.

"""

Steps_text = """
STEP 1: Click on the Keylogger tool button, a new window will pop up on screen.

STEP 2: A small window will pop up on screen containing start and stop button in it.

STEP 3: Click on the start button.

STEP 4: The Output will be displayed on the screen which include list of pressed 
             keystrokes with accurate date and time.

STEP 5: It stop click on the STOP button.
"""

Insights_text = """Advantages:

  1. Captures keystrokes, potentially revealing sensitive information.
  2. Useful for monitoring and tracking user activities.
  3. Forensic Investigation: Assists in forensic analysis for security incidents.


Disadvantages:

  1. Considered invasive and a breach of privacy if used without consent.
  2. Can be detected by antivirus or security software.
  3. Legal Implications: Unauthorized use violates privacy laws and ethical 
      standards.
"""

Application_text = """Applications:

1. Activity Monitoring: Recording keystrokes for monitoring user activity.
2. Surveillance: Tracking user actions on a device for security or investigative 
    purposes.
3. Forensic Analysis: Assisting in digital forensic investigations by capturing user 
    input.
"""

Result = PhotoImage(file= 'D:\\Multipurpose Cybersecurity Tool\\UI\\03_tools manual\\Result_Images\\Keylogger3.png')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

window.mainloop()