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

label = tk.Label(window, text="DISTRIBUTED DENIAL OF SERVICE", font=('Inter', 30, 'bold'), fg='#000f46')
label.place(x=220, y=30)

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
    file_path = "D:\\Multipurpose Cybersecurity Tool\\Tools\\miniddos2.py"

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
A DDoS (Distributed Denial of Service) Mini Tool is a type of software or 
application designed to conduct a small-scale DDoS attack. DDoS attacks involve 
overwhelming a target's online service, such as a website or server, with an 
excessive amount of traffic. The "Mini" designation may imply that it is a 
scaled-down version, but it still aims to disrupt the normal functioning of the 
targeted service by flooding it with a high volume of requests. It's crucial to 
note that engaging in DDoS attacks is illegal and unethical, as it can cause 
significant harm to online services and violate the terms of use of internet 
service providers. Legal consequences and severe penalties may result from the 
use of DDoS tools for malicious purposes.

Imagine you're having a picnic with friends, and suddenly, a swarm of bees 
overwhelms everything, making it chaotic. A DDoS Mini Tool is like sending lots 
of bees (data requests) to a website or an online service all at once. It's not 
letting the website breathe and serve its regular visitors because it's flooded 
with too many requests. This can make the website slow or even crash, causing a 
virtual traffic jam.
"""

Steps_text = """
STEP 1: Click on the DDOS tool button, a new window will pop up on screen and 
             check that you have legal authorization.

STEP 2: Enter URL of website in the dialogue box.

STEP 3: Enter Number of threads (ex- 5,10,etc).

STEP 4: It will start threads in sequence.

STEP 5: The Output will be displayed on the screen which include list of 
             treads with status code.

STEP 6: select EXIT option to stop the tool.
"""

Insights_text = """Advantages:

 1. Disrupts target services or websites by overwhelming them with traffic.
 2. Used for testing network resilience or in some cases, as a protest.
 3. Protest Mechanism: Used as a form of protest in some cases.


Disadvantages:

 1. Illegal and unethical when used without authorization.
 2. Can cause severe financial losses and damage to reputations.
 3. Financial Losses: Results in significant financial losses due to service downtime.
"""

Application_text = """Applications:

1. Service Disruption: Overwhelming target services to cause downtime.
2. Resilience Testing: Testing network resilience against high traffic loads.
3. Protest Mechanism: Used as a form of protest to disrupt services.
"""

Result = PhotoImage(file= 'D:\\Multipurpose Cybersecurity Tool\\UI\\03_tools manual\\Result_Images\\DDOS.png')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

window.mainloop()