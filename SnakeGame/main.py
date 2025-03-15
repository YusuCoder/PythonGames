from traceback import print_tb
from turtle import Screen
import random
import scoreboard
import time

import scoreboard
import snake
import food

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake")


snake = snake.Snake()
food = food.Food()
score = scoreboard.Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 20:
        food.new_food()
        score.update_score()
        snake.add_tail()
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        score.game_over()
        game = False
    if snake.check_tail_collision():
        score.game_over()
        game = False

screen.exitonclick()