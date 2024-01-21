
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess
import time

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\\Multipurpose Cybersecurity Tool\\UI\\01_Opening Screen\\assets\\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Multipurpose cybersecurity Tool")
window.iconbitmap("D:\\Multipurpose Cybersecurity Tool\\logo.ico")

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
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    545.0,
    251.0,
    image=image_image_1
)

def open_specific_file():

    window.after(100, window.destroy)
    
    # Specify the path to the Python script you want to open
    file_path = "D:\\Multipurpose Cybersecurity Tool\\UI\\02_Dashboard\\gui.py"

    # Use subprocess to execute the Python script
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
    command=open_specific_file,
    relief="flat"
)

button_1.place(
    x=404.0,
    y=483.0,
    width=272.0,
    height=54.0
)

window.mainloop()
