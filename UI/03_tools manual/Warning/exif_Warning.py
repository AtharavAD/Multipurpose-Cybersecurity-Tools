import tkinter as tk
from tkinter import PhotoImage
import subprocess

window = tk.Tk()
window.resizable(False, False)
window.title("Warning!!")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width - 550) // 2
y_coordinate = (screen_height - 350) // 2
window.geometry(f"550x320+{x_coordinate}+{y_coordinate}")

def para():
    para_text = (
        "This tool is intended for educational purposes only. Unauthorized\n"
        "use of this tool on systems or networks that you do not own or\n"
        "have explicit permission to test is strictly prohibited. The misuse\n"
        "of this tool for malicious activities is against the law and can\n"
        "result in severe legal consequences.\n"
        "\n"
        "By using this tool, you agree to:\n"
        "\n"
        "1. Use it solely for educational and ethical hacking purposes\n"
        "2. Respect the privacy and security of others\n"
        "3. Obtain explicit authorization before testing any system or network\n"
    )
    
    paragraph_label.config(text=para_text)

paragraph_label = tk.Label(window, text="", font=('Arial', 13), fg='#000f46', justify='left')
paragraph_label.place(x=25, y=20)

def open_specific_file():
    # Specify the path to the Python script you want to open
    file_path = "D:\\Major Project\\New Tools\\NNmap.py"

    # Use subprocess to execute the Python script
    try:
        subprocess.Popen(["python", file_path], shell=True)
        window.destroy()  # Destroy the window after opening the specific file
    except Exception as e:
        print("Error:", e)

agree_btn = tk.Button(window, text='I agree',
                             font=('Arial',13,'bold'), fg='#e5e5e5', bd=0, bg='#000f46',
                             command=open_specific_file)
agree_btn.place(x=230, y=260)

# Call the para function to update the text when the window is created
para()

# Start the Tkinter event loop
window.mainloop()
