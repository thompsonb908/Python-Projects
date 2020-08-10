import tkinter as tk
import random

window = tk.Tk()

window.rowconfigure(
    [0,1],
    minsize=50,
    weight=1
)
window.columnconfigure(
    0,
    minsize=150,
    weight=1
)

lbl_value = tk.Label(
    master=window,
    text='0'
)
lbl_value.grid(
    row=1,
    column=0,
    sticky="nsew"
)

def randomNumber():
    lbl_value["text"] = str(random.randint(1,6))

btn_roll = tk.Button(
    master=window,
    text="Roll",
    command=randomNumber
)

btn_roll.grid(
    row=0,
    column=0,
    sticky="nsew"
)

window.mainloop()