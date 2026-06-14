from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    title.config(text = "Timer")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    count_down(work_sec)
    if reps % 8 == 0:
        count_down(long_break_sec)
        title.config(text = f"BREAK", fg = RED, bg = YELLOW)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title.config(text = f"BREAK", fg = PINK, bg = YELLOW)
    else:
        count_down(work_sec)
        title.config(text = f"BREAK", fg = GREEN, bg = YELLOW)

    count_down(1 * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 1:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.configure(padx = 20, pady = 20, bg = YELLOW)


title = Label(text = "Pomodoro Timer",fg = GREEN ,font = (FONT_NAME, 50, "bold"), bg = YELLOW)
title.grid(row = 0, column = 1)


canvas = Canvas(window, width=200, height=224, bg = YELLOW, highlightthickness = 0)
tomato_img= PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text (100,130,text= "00:00", fill = "white", font =(FONT_NAME, 35, "bold"))
canvas.grid(row = 1, column = 1)


start_button = Button(text = "start", highlightthickness=0, font= (FONT_NAME, 10), command = start_timer)
start_button.grid(row = 2, column = 0)
reset_button = Button(text = "reset", highlightthickness=0, font = (FONT_NAME,10), command = reset_timer)
reset_button.grid(row = 2, column = 2)

check_mark = Label(text = "✔️", fg = GREEN, bg = YELLOW, highlightthickness = 0, font = (FONT_NAME, 25, "bold"))
check_mark.grid(row = 3, column = 1)


window.mainloop()

