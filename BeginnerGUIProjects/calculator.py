from tkinter import *
import pandas
from random import randint, choice, shuffle
import random
from pandas.core.interchange import column

# ______________________UI SETUP________________________
window = Tk()
window.title("Calculator")
window.configure(padx = 10, pady = 10, background= "white")

canvas = Canvas(window, width = 500, height = 500, bg = "white", highlightthickness = 0)
image1 = PhotoImage(file = "calc_bg.png")
canvas_bg = canvas.create_image(250,250,image = image1, anchor = "center")

display = Entry(
    window,
    width=12,
    font=("Arial", 24, "bold"),
    justify="right",
    bd=0,
    bg="#B7D7B7",
    fg="#3A6B4A",
    insertbackground="#3A6B4A",  # cursor color
    relief="flat"
)
canvas.create_window(250, 110, window=display)
# ______________________BUTTON FUNC________________________
def button_click(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, current + str(number))

def button_click2(value):
    current = display.get()
    display.delete(0, END)
    display.insert(0, current + str(value))


def calculate():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, END)
        display.insert(0, str(result))
    except:
        display.delete(0, END)
        display.insert(0, "Error")


def clear():
    display.delete(0, END)
# ______________________BUTTON SETUP________________________

btn1 = Button(window, text="1", width=5, height=2, command=lambda: button_click(1))
canvas.create_window(145, 230, window=btn1)
btn2 = Button(window, text="2", width=5, height=2, command=lambda: button_click(2))
canvas.create_window(205, 230, window=btn2)
btn3 = Button(window, text="3", width=5, height=2, command=lambda: button_click(3))
canvas.create_window(265, 230, window=btn3)
btn4 = Button(window, text="+", width=5, height=2,command=lambda: button_click2("+"))
canvas.create_window(355, 230, window=btn4)
btn5 = Button(window, text="4", width=5, height=2, command=lambda: button_click(4))
canvas.create_window(145, 295, window=btn5)
btn6 = Button(window, text="5", width=5, height=2, command=lambda: button_click(5))
canvas.create_window(205, 295, window=btn6)
btn7 = Button(window, text="6", width=5, height=2, command=lambda: button_click(6))
canvas.create_window(265, 295, window=btn7)
btn8 = Button(window, text="-", width=5, height=2,command=lambda: button_click2("-"))
canvas.create_window(355, 295, window=btn8)
btn9 = Button(window, text="7", width=5, height=2, command=lambda: button_click(7))
canvas.create_window(145, 355, window=btn9)
btn10 = Button(window, text="8", width=5, height=2, command=lambda: button_click(8))
canvas.create_window(205, 355, window=btn10)
btn11 = Button(window, text="9", width=5, height=2, command=lambda: button_click(9))
canvas.create_window(265, 355, window=btn11)
btn12 = Button(window, text="*", width=5, height=2, command=lambda: button_click2("*"))
canvas.create_window(355, 355, window=btn12)
btn13 = Button(window, text="/", width=5, height=2, command=lambda: button_click2("/"))
canvas.create_window(145, 420, window=btn13)
btn14 = Button(window, text="0", width=5, height=2, command=lambda: button_click2("0"))
canvas.create_window(205, 420, window=btn14)
btn15 = Button(window, text="=", width=5, height=2,  command=calculate)
canvas.create_window(265, 420, window=btn15)
btn16 = Button(window, text="C", width=5, height=2, command=clear)
canvas.create_window(355, 420, window=btn16)




canvas.grid()
window.mainloop()