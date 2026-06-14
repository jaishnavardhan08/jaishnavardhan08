from turtle import Turtle, Screen

timmy_turtle = Turtle()
timmy_turtle.shape("turtle")
timmy_turtle.color("red")
for _ in range(4):
    timmy_turtle.forward(100)
    timmy_turtle.right(90)
screen = Screen()
screen.exitonclick()