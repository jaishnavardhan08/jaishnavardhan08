import turtle as t
import random
tim = t.Turtle()

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
screen = t.Screen()
screen.exitonclick()
num_sides = 10