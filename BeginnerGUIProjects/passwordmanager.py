from tkinter import *
import string
from tkinter import messagebox
from random import choice, randint, shuffle
from pandas.core.interchange import column
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not any(char in string.punctuation for char in password):
        messagebox.showerror(
            title="Invalid Password",
            message="Password must contain at least one symbol."
        )
        return
    else:
        messagebox.showinfo(title= "Error", message = "ARE YOU SURE YOU WANNA SAVE YOUR PASSWORD?")

    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}" + "\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx = 10, pady = 10)
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row = 0, column = 1)
# LABELS
password_label = Label(window, text = "Password")
password_label.grid(row = 4, column = 0)
email_label = Label(window, text = "Email/Username")
email_label.grid(row = 3, column = 0)
website_label = Label(window, text = "Website")
website_label.grid(row = 2, column = 0)
#ENTRIES
website_entry = Entry(width = 35)
website_entry.grid(row = 2, column = 1, columnspan = 2)
website_entry.focus()
email_entry = Entry(width = 35)
email_entry.grid(row = 3, column = 1, columnspan = 2)
email_entry.insert(0 ,"jaishna.vardhan08@gmail.com")
password_entry = Entry (width = 21)
password_entry.grid(row = 4, column = 1, columnspan = 2)
# BUTTONS
password_generation_button = Button(text= "generate", command = generate_password)
password_generation_button.grid(row = 4, column = 2)
add_button = Button(text = "ADD", width = 35, command= save)
add_button.grid(row = 5, column = 1)
window.mainloop()