import tkinter as tk

labels = {
    0:"First Name:",
    1:"Last Name:",
    2:"Address Line 1:",
    3:"Address Line 2:",
    4:"City:",
    5:"State/Province:",
    6:"Postal Code:",
    7:"Country:"
}
window = tk.Tk()
window.title("Address Entry Form")

frm_form = tk.Frame(
    relief=tk.SUNKEN,
    borderwidth=3
)
frm_form.pack()

for i in range(len(labels)):
    label = tk.Label(
        master=frm_form,
        text=labels.get(i)
    )
    entry = tk.Entry(
        master=frm_form,
        width=50
    )
    label.grid(row=i,column=0,sticky="e")
    entry.grid(row=i,column=1)

fmr_buttons = tk.Frame()
fmr_buttons.pack(
    fill=tk.X,
    ipadx=5,
    ipady=5
)

btn_submit = tk.Button(
    master=fmr_buttons,
    text="Submit"
)
btn_submit.pack(
    side=tk.RIGHT,
    padx=10,
    ipadx=10
)

btn_clear = tk.Button(
    master=fmr_buttons,
    text="Clear"
)
btn_clear.pack(
    side=tk.RIGHT,
    ipadx=10
)

window.mainloop()