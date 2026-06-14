from tkinter import *

def miles_to_kilometers():
    miles = float(miles_input.get())
    kilometer = miles * 1.609
    kilometer_result_label.config(text= f"{kilometer}")



window = Tk()
window.title("Miles to Kilometer")

miles_input = Entry(width= 5)
miles_input.grid(row=0, column=1)
window.config(padx=20, pady=20)

miles_label = Label(window, text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = Label(window, text="Equals: ")
is_equal_label.grid(row=1, column=0)

kilometer_result_label = Label(window, text="0")
kilometer_result_label.grid(row=1, column=1)

kilometers_label = Label(window, text="Kilometers")
kilometers_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate", command=miles_to_kilometers)
calculate_button.grid(row=2, column=1)


window.mainloop()

