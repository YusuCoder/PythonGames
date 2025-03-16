import random
from turtle import Turtle, Screen
from ball import Ball
from collisions import WallCollisions
from paddle import Paddle
from field import Field
import time

screen = Screen()
turtle = Turtle()
line_turtle = Turtle()
screen.setup(1500, 800)
screen.bgcolor("black")
screen.tracer(0)


paddle = Paddle()
paddle.paddle()
screen.listen()
ball = Ball()
field = Field(screen)
wall_c = WallCollisions(screen, ball, paddle)
field.draw_line()
field.create_scores()

key_state = {"Up": False, "Down": False}

screen.onkey(paddle.move_up_left_paddle, "Up")
screen.onkey(paddle.move_down_left_paddle, "Down")
screen.onkey(paddle.move_up_right_paddle, "w")
screen.onkey(paddle.move_down_right_paddle, "s")
# Function to keep the game running

def game_loop():
    ball.move_ball()
    wall_c.check_walls()
    wall_c.paddle_collision()
    screen.update()
    screen.ontimer(game_loop, 20)
    if ball.xcor() >= 750 or ball.xcor() <= -750:
        if ball.xcor() <= -750:
            field.scores[1] += 1
            field.update_score()
        elif ball.xcor() >= 750:
            field.scores[0] += 1
            field.update_score()
        ball.reset_direction()
        screen.update()
        time.sleep(2)
# Call game_loop() every 20ms

# Start the game
game_loop()
screen.mainloop()

