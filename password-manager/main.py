from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


def find_password():
    website = website_entry.get()
    try:
        with open('data.json') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Oops', message='Data File Not Found.')
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f'Email: {email}\nPassword: {password}')
        else:
            messagebox.showinfo(title='Error', message=f'No details for the {website} exists.')
    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'w', 'v', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]
    number_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letter_list + symbol_list + number_list
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()
    new_data = {
        website_data: {
            'email': email_data,
            'password': password_data,
        }
    }

    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title='Oops', message="You left website or password field empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
                # Updating old data with new data
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                # Saving data
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                # Saving data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password generator')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=20)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, 'muhammad.mamleeev1998@gmail.com')

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text='Generate Password', command=generate_password)
generate_password_button.grid(column=2, row=3)

search_button = Button(text='Search', width=14, command=find_password)
search_button.grid(column=2, row=1)

add_button = Button(text='Add', width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
