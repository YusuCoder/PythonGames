import random
from turtle import Turtle, Screen
from ball import Ball
from collisions import WallCollisions
from paddle import Paddle

screen = Screen()
turtle = Turtle()
screen.setup(1500, 800)
screen.bgcolor("black")
screen.tracer(0)


paddle = Paddle()
paddle.paddle()
screen.listen()
ball = Ball()
wall_c = WallCollisions(screen, ball, paddle)


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
    screen.ontimer(game_loop, 20)  # Call game_loop() every 20ms

# Start the game
game_loop()
screen.mainloop()

