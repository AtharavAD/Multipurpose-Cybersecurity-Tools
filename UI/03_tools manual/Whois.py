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

label = tk.Label(window, text="               WHOIS", font=('Inter', 30, 'bold'), fg='#000f46')
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
    file_path = "D:\\Multipurpose Cybersecurity Tool\\Tools\\MyWhois2.py"

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
Introduction_text = """WHOIS is a protocol and database system used to look up information about 
domain names and IP addresses. It provides details about the registered owner of 
a domain, their contact information, domain registration and expiration dates, 
and the domain's name servers. This information is stored in a publicly 
accessible database and is useful for various purposes such as identifying the 
owner of a website, contacting domain administrators for technical issues or 
business inquiries, and investigating cybersecurity incidents.

To perform a WHOIS lookup, you can use WHOIS lookup tools available on various
websites. These tools allow you to query the WHOIS database by entering a 
domain name or IP address. The results will provide you with information about 
the domain's registrant, registrar, registration and expiration dates, and
sometimes, the domain's administrative and technical contacts.

It's important to note that in recent years, privacy concerns have led to 
changes in WHOIS policies. Some domain registrars offer WHOIS privacy services, 
also known as WHOIS masking or private registration, which allows domain owners 
to keep their personal information private by replacing it with the registrar's 
contact information in the public WHOIS database.
"""

Steps_text = """STEP 1: Click on the Whois tool button, a new window will pop up on screen.

STEP 2: Enter the domain name in URL format in the dialogue box and press enter.

STEP 3: It will start scanning.

STEP 4: The Output will be displayed on the screen which include every detail 
             about the entered domain name.

STEP 5: It will ask to enter another lookup.

STEP 6: To Continue enter new domain name and repeat process and for Exit 
             press enter key.
"""

Insights_text = """Advantages:

  1. Retrieves domain ownership and contact details.
  2. Assists in identifying website administrators or domain registrants.
  3. Security Insights: Provides insights into potential security risks related to 
     domains.


Disadvantages:

 1. Limited or obfuscated information in some cases.
 2. Privacy concerns as personal details may be exposed.
 3. Misuse:  Data obtained can be misused for spamming or other unauthorized 
    activities.
"""

Application_text = """Applications:

1. Domain Information: Retrieving ownership and administrative details of domains.
2. Network Analysis: Identifying domain-related information for investigative 
    purposes.
3. Security Insights: Providing insights into potential security risks related to 
    domains."""

Result = PhotoImage(file= 'D:\\Multipurpose Cybersecurity Tool\\UI\\03_tools manual\\Result_Images\\Whois2.png')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

window.mainloop()