from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200) # Padding

#Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0) # Top left corner
my_label.config(padx=50, pady=50)

#Button
button = Button(text="Button", command=button_clicked)
button.grid(column=1, row=1)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

#Button 2
button = Button(text="New Button", command=button_clicked)
button.grid(column=2, row=0)


window.mainloop()
# Tkinter has a lot of layout managers that defines how to position each of the widgets:
'''
If a widget is created but it doesn't have any layout manager, it won't be shown
1.  Pack
Packs each of the widgets next to each other in a logical manner.
Instead packing them fro the top you can change the side parameter in the function
However, it is difficult to have a precise position
pack()

2. Place
All about precise position
However, it is super specific. 
It becomes a nightmare to arrange 50 widgets 
place()

3. Grid
Imagines that entire program is a grid
You can split the screen into any amount of rows and columns you want
This is relative to the other widgets. So if you only have one widget in will start off on the top left
You can't mix up grid and pack, it gives an error
grid(column = , row = )
'''
