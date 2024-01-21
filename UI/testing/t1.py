import tkinter as tk

def Introduction_page():
    Introduction_frame = tk.Frame(main_frame)

    text = "Introduction page\n\nThis is a multi-line introduction text.\nYou can add more lines as needed."

    lb = tk.Label(Introduction_frame, text=text, font=('Inter', 12), fg='#000f46', bg='#e5e5e5', justify='left')
    lb.pack()

    Introduction_frame.pack(pady=20)

# Create the main window
root = tk.Tk()
root.title("My Application")

# Create the main frame
main_frame = tk.Frame(root)

# Call the function to create the introduction page
Introduction_page()

# Run the Tkinter event loop
root.mainloop()
