import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
tim = Turtle()
screen.setup(width=500,height=400)
user_bet= screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race: Enter the colour")
colors= ["red","orange","yellow","green","blue","indigo","violet"]
y_positions = [-70,-40,-10,20,50,80,110]
all_turtles = []
for turtle_index in range(0,7):
    new_turtle = Turtle(shape= "turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-250, y = y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! {winning_color} won the race!")
            else:
                print(f"You lose! {winning_color} won the race!")
            print(turtle.color())

        rand_distance= random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()




