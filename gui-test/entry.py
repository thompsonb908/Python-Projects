import tkinter as tk

top = tk.Tk()

frame = tk.Frame(
    master=top,
    borderwidth=5
)

entry_name = tk.Entry(
    master=frame,
    width=40,
    fg='black',
    bg='white'
)
entry_name.insert(0,"What is your name?")

frame.pack()
entry_name.pack()
top.mainloop()