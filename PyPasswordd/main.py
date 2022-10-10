import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import os

EMAIL = "4aditya.m@gmail.com"


def browse():
    os.startfile(r'C:\Users\mahes\PycharmProjects\PyPasswordd\Manager.json')


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():

    website = website_input.get().lower()
    username = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode='r') as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", mode='w') as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)
            with open("data.json", mode='w') as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_input.delete(0, 'end')
            website_input.focus()
            username_input.delete(0, 'end')
            password_input.delete(0, 'end')
            username_input.insert(0, EMAIL)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PyPass Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1, columnspan=2)

website_label = Label(text="Website(URL): ")
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username: ")
username_label.grid(row=2, column=0)
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

website_input = Entry(width=52)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()
username_input = Entry(width=52)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, EMAIL)
password_input = Entry(width=33)
password_input.grid(column=1, row=3)

generate_password = Button(text="Generate Password", command=generate)
generate_password.grid(column=2, row=3, sticky='EW')
add = Button(text="Add", width=44, command=add_data)
add.grid(column=1, row=4, columnspan=2)
browse_db = Button(text="Browse", width=44, command=browse)
browse_db.grid(column=1, row=5, columnspan=2)

window.mainloop()
