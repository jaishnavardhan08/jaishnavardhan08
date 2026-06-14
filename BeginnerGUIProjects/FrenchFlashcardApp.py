BACKGROUND_COLOR = "#B1DDC6"
FONT_COLOR = "#3B7597"
BLACK = "#000000"

from tkinter import *
import string
from tkinter import messagebox
from random import randint,choice, shuffle
import pandas
from pandas.core.interchange import column
import random

data = pandas.read_csv("data.csv")
to_learn = data.to_dict(orient = "records")
current_card = {}
# ---------------------------- FLIPPING THE CARDS ------------------------------- #
#             ~~~~~~~~~~~~ FRENCH CARDS  ~~~~~~~~~~~~            #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(flashy_title, text = "French", fill = FONT_COLOR)
    canvas.itemconfig(word_text, text = current_card["French"], fill = FONT_COLOR)
    canvas.itemconfig(card_background, image = image1)
    flip_timer= window.after(3000, func=flip_card)
#             ~~~~~~~~~~~~ ENGLISH CARDS ~~~~~~~~~~~~           #
def flip_card():
    canvas.itemconfig(flashy_title, text = "English",fill = BLACK)
    canvas.itemconfig(word_text, text = current_card["English"], fill = BLACK )
    canvas.itemconfig(card_background, image = image2)
# ---------------------------- SAVING THE NOT KNOWNS ------------------------------- #
def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv")
    next_card()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("FRENCH FLASHCARDS")
window.configure(padx = 50, pady = 50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func = flip_card)

canvas = Canvas(window,width=800, height=526, bg = BACKGROUND_COLOR, highlightthickness = 0 )
image1 = PhotoImage(file= "card_front.png")
image2 = PhotoImage(file= "card_back.png")
card_background = canvas.create_image(400, 263, image = image1)
canvas.grid(row = 0, column = 0, columnspan = 2)
flashy_title = canvas.create_text(400, 150, text = "",font = ("Ariel", 60, "bold", "italic"), fill = FONT_COLOR)
word_text = canvas.create_text(400, 263, text = "", font = ("Ariel", 40, "bold"), fill = FONT_COLOR)

# ---------------------------- BUTTON SETUP ------------------------------- #
tick_image = PhotoImage(file= "right.png")
tick_button = Button(image = tick_image, command = next_card)
tick_button.config(highlightthickness = 0)
tick_button.grid(row = 1, column = 0)
cross_image = PhotoImage(file = "wrong.png")
cross_button = Button(image = cross_image, command = next_card)
cross_button.config(highlightthickness = 0)
cross_button.grid(row = 1, column = 1)

next_card()
canvas.grid()
window.mainloop()