# hello-world.py
# Gui based hello world program

import tkinter as tk

window = tk.Tk()

label1 = tk.Label(
    text = "Hello, Tkinter",
    fg="white",
    bg="black",
    width=10,
    height=10
)

label2 = tk.Label(
    text="Name"
)

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg='blue',
    fg='yellow'
)

entry = tk.Entry()

# label1.pack()
# button.pack()
label2.pack()
entry.pack()

window.mainloop()