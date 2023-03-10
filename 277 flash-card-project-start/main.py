from tkinter import *
import pandas
from random import choice


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# ---------------------------- READING DATA ------------------------------- #
try:
    data = pandas.read_csv("data/word to learn.csv")
except FileNotFoundError:
    start_data = pandas.read_csv("data/french_words.csv")
    to_learn = start_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)         # таймер сбрасывается, если нажимать на конпку раньше чем через 3 сек
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    canvas.itemconfig(card_bg, image=card_front)
    flip_timer = window.after(3000, func=card_flip)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/words to learn.csv', index=False)
    next_card()


def card_flip():
    canvas.itemconfig(card_bg, image=card_back)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=card_flip)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
card_bg = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='word', font=('Ariel', 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
right_image = PhotoImage(file='images/right.png')
known_button = Button(image=right_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

wrong_image = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

next_card()

window.mainloop()
