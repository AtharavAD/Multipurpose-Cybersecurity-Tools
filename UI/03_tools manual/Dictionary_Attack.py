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

label = tk.Label(window, text="     Dictionary Attack", font=('Inter', 30, 'bold'), fg='#000f46')
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
    file_path = "D:\\Multipurpose Cybersecurity Tool\\Tools\\NDictionaryAttack.py"

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
Introduction_text = """A dictionary attack is a type of cyberattack that involves systematically trying a list 
of precompiled passwords, phrases, or combinations against a target system, 
such as an account login or encryption key. Unlike a brute force attack, which 
exhaustively tries all possible combinations, a dictionary attack uses a 
specific set of known words, phrases, or common passwords to gain unauthorized 
access. This method takes advantage of the tendency of many users to use easily 
guessable passwords, making it a more efficient alternative to random guessing. 
Countermeasures against dictionary attacks include password complexity 
requirements and account lockout policies.

Imagine you have a list of possible passwords, like "123456," "password," or 
"qwerty." A dictionary attack is like trying each of these passwords one by one 
until you find the right one. It's not as random as a brute force attack; 
instead, it's like checking a predefined list of common passwords to see if any 
of them work.
"""

Steps_text = """STEP 1: Click on the Dictionary Attack tool button, a new window will pop up on 
             screen.

STEP 2: Enter the password in the available dialogue box.

STEP 3: Press the Check Password button which is present below the dialogue 
             box.

STEP 4: The details regarding the password will be provided.

STEP 5: It will analyze and display the output regarding password like it's weak 
             or strong, it's category list and time taken guess the password.

STEP 6: To repeat enter the new password and to stop select exit option.
"""

Insights_text = """Advantages:

  1. Efficient in cracking passwords using pre-generated wordlists.
  2. Reveals weak or commonly used passwords.
  3. Ease of Implementation: Available in numerous tools and easy to execute.


Disadvantages:

  1. Ineffective against complex or unique passwords.
  2. Can be detected and prevented by security measures.
  3. Legal Concerns: Unauthorized use leads to legal repercussions.
"""

Application_text = """Applications:

1. Password Guessing: Trying predefined wordlists to crack passwords.
2. Weakness Identification: Identifying and exploiting commonly used or weak passwords.
3. Authentication Testing: Testing systems against known dictionary terms for security assessment.
"""

Result = PhotoImage(file= 'D:\\Multipurpose Cybersecurity Tool\\UI\\03_tools manual\\Result_Images\\Dictionary3.png')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

window.mainloop()