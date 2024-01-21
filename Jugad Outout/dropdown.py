import tkinter as tk

def on_button_click():
    print(entry.get())  # Get the text entered in the Entry widget

root = tk.Tk()
root.title("Entry Box Example")

# Create an Entry widget
entry = tk.Entry(root)

# Specify the desired location using the place method
entry.place(x=50, y=50)

# Create a button to demonstrate getting the text from the Entry widget
button = tk.Button(root, text="Get Text", command=on_button_click)
button.place(x=50, y=80)

root.mainloop()
