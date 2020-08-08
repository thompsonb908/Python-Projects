# hello-world.py
# Gui based hello world program

from tkinter import *

window = Tk()

label1 = Label(
    text = "Hello, Tkinter",
    fg="white",
    bg="black",
    width=10,
    height=10
)

label2 = Label(
    text="Name"
)

button = Button(
    text="Click me!",
    width=25,
    height=5,
    bg='blue',
    fg='yellow'
)

entry = Entry()

# label1.pack()
# button.pack()
label2.pack()
entry.pack()

window.mainloop()
name = entry.get()
print(name)