import random
from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
import degrees

screen = Screen()
turtle = Turtle()
screen.setup(1500, 800)
screen.bgcolor("black")
screen.tracer(0)


paddle = Paddle()
paddle.paddle()
screen.listen()
ball = Ball()


screen.onkey(paddle.move_up_left_paddle, "Up")
screen.onkey(paddle.move_down_left_paddle, "Down")
screen.onkey(paddle.move_up_right_paddle, "w")
screen.onkey(paddle.move_down_right_paddle, "s")
# Function to keep the game running

def game_loop():
    ball.move_ball()
    if ball.ycor() >= 380 and ball.xcor() >= -10:
        if not ball.hit_wall:
            new_dir = random.choice(degrees.directions['right_bottom'])
            ball.setheading(new_dir)
            ball.hit_wall = True
            print(f"right = {new_dir}")
    elif ball.ycor() <= -380 and ball.xcor() >= -10:
        if not ball.hit_wall:
            new_dir = random.choice(degrees.directions['right_top'])
            ball.setheading(new_dir)
            ball.hit_wall = True
            print(f"right = {new_dir}")
    elif ball.ycor() >= 380 and ball.xcor() <= 10:
        if not ball.hit_wall:
            new_dir = random.choice(degrees.directions['left_bottom'])
            ball.setheading(new_dir)
            ball.hit_wall = True
            print(f"left= {new_dir}")
    elif ball.ycor() <= -380 and ball.xcor() <= 10:
        if not ball.hit_wall:
            new_dir = random.choice(degrees.directions['left_top'])
            ball.setheading(new_dir)
            ball.hit_wall = True
            print(f"left= {new_dir}")

    if not (ball.ycor() >= 380 or ball.ycor() <= -380 ):
        ball.hit_wall = False
        print("here")

    screen.update()
    screen.ontimer(game_loop, 20)  # Call game_loop() every 20ms

# Start the game
game_loop()

# Keep window open
screen.mainloop()

# while True:
#     ball.move_ball()
#     screen.update()

# screen.exitonclick()

