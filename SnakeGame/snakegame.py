import time
from turtle import Screen
from food import Food
from main import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,key = "Up")
screen.onkey(snake.down,key ="Down")
screen.onkey(snake.left,key ="Left")
screen.onkey(snake.right,key="Right")



game_is_on= True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
#when snake and food collides
    if snake.head.distance(food) < 15:
        print("nomnomnom")
        food.refresh()
        scoreboard.increase_score()
    # collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    # collision of snake with it's own tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()