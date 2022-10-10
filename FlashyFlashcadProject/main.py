from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
SEC = 10
timer = None
to_learn = {}
word = {}
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def is_known():
    to_learn.remove(word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()


def next_card():
    global word, timer
    if timer is not None:
        window.after_cancel(timer)
    word = random.choice(to_learn)
    canvas.itemconfig(flashy_title, text="French", fill="black")
    canvas.itemconfig(flashy_word, text=word["French"], fill="black")
    canvas.itemconfig(back_ground, image=front_img)
    window.after(0, count_down, SEC)


def flip_card():
    canvas.itemconfig(back_ground, image=back_img)
    canvas.itemconfig(flashy_title, fill="white", text="English")
    canvas.itemconfig(flashy_word, fill="white", text=word["English"])


def count_down(count):
    global timer
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
        canvas.itemconfig(count_label, text=count)
    else:
        canvas.itemconfig(count_label, text="")
        flip_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window.after(0, count_down, SEC)

canvas = Canvas(width=800, height=525, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
back_ground = canvas.create_image(400, 262.5, image=front_img)
count_label = canvas.create_text(400, 262.5, text="", font=("Calibri", 500, "bold"), fill=BACKGROUND_COLOR)
flashy_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"), fill="black")
flashy_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

right_img = PhotoImage(file="images/right.png")
correct_btn = Button(image=right_img, highlightthickness=0, command=is_known, bd=0)
correct_btn.grid(row=1, column=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=next_card, bd = 0)
wrong_btn.grid(row=1, column=0)

next_card()

window.mainloop()
