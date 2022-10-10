from tkinter import *


def calculate_m():
    input_val = float(input.get())
    output_val = round(input_val * 1.609, 3)
    output.config(text=f"{output_val}")


def calculate_k():
    input_val = float(input.get())
    output_val = round(input_val / 1.609, 3)
    output.config(text=f"{output_val}")


def switch():
    input_label["text"], output_label["text"] = output_label["text"], input_label["text"]
    if input_label["text"] == "Miles":
        button["command"] = calculate_m
    else:
        button["command"] = calculate_k


window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(100, 100)
window.config(padx=50, pady=50)

input = Entry(width=10)
input.grid(column=1, row=0)

input_label = Label(text="Miles")
input_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

output = Label(text="0")
output.grid(column=1, row=1)

output_label = Label(text="Km")
output_label.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate_m)
button.grid(column=1, row=2)

switch = Button(text="Switch", command=switch)
switch.grid(column=2, row=2)
window.mainloop()
