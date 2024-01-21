import tkinter as tk

window = tk.Tk()
window.resizable(False, False)
window.title("Foot Printing")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width - 800) // 2
y_coordinate = (screen_height - 450) // 2
window.geometry(f"750x450+{x_coordinate}+{y_coordinate}")

def para():
    para_text = (
        "Enter the target URL: \n"
        "\n"
        """Port 21 is closed.
Port 22 is open.
Port 25 is open.
Port 53 is open.
Port 80 is open.
Port 110 is open.
Port 143 is open.
Port 443 is open.
Port 445 is closed.
Port 3389 is closed.
Port 3306 is open.
Port 5432 is closed.
Port 123 is closed.\n"""
"\n"
"\n"
"Do you want to scan another target? (yes/no): \n"  
    )
    
    paragraph_label.config(text=para_text)

paragraph_label = tk.Label(window, text="", font=('Arial', 13), fg='#000f46', justify='left')
paragraph_label.place(x=25, y=20)

para()

entry1 = tk.Entry(window, show="", width=35)
entry1.place(x=200, y=23)

entry1 = tk.Entry(window, show="", width=15)
entry1.place(x=370, y=348)

# Start the Tkinter event loop
window.mainloop()
