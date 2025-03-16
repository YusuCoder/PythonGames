from turtle import Turtle
import random
from ball import Ball
import degrees
PADDLE_HEIGHT = 110
PADDLE_WIDTH = 30


class WallCollisions:
    def __init__(self, screen, ball, paddle):
        super().__init__()
        self.screen = screen
        self.ball = ball
        self.paddle = paddle
        self.hit_wall = False

    def check_walls(self):
        """**Checks upper and lower walls collisions"""
        if self.ball.ycor() >= 380 and self.ball.xcor() >= -10:
            if not self.hit_wall:
                new_dir = random.choice(degrees.directions['right_bottom'])
                self.ball.setheading(new_dir)
                self.hit_wall = True
        elif self.ball.ycor() <= -380 and self.ball.xcor() >= -10:
            if not self.hit_wall:
                new_dir = random.choice(degrees.directions['right_top'])
                self.ball.setheading(new_dir)
                self.hit_wall = True
        elif self.ball.ycor() >= 380 and self.ball.xcor() <= 10:
            if not self.hit_wall:
                new_dir = random.choice(degrees.directions['left_bottom'])
                self.ball.setheading(new_dir)
                self.hit_wall = True
        elif self.ball.ycor() <= -380 and self.ball.xcor() <= 10:
            if not self.hit_wall:
                new_dir = random.choice(degrees.directions['left_top'])
                self.ball.setheading(new_dir)
                self.hit_wall = True

        if not (self.ball.ycor() >= 380 or self.ball.ycor() <= -380):
            self.hit_wall = False

    def paddle_collision(self):
        """**Checks paddle collisions"""
        left_paddle = self.paddle.paddles[0].ycor()
        right_paddle = self.paddle.paddles[1].ycor()
        ball_x = self.ball.xcor()
        ball_y = self.ball.ycor()

        # Collision check with Left Paddle
        if 700 <= ball_x <= 720 and (left_paddle + PADDLE_HEIGHT / 2 >= ball_y >= left_paddle - PADDLE_HEIGHT / 2):
            self.ball.setheading(self.ball.towards(random.choice(degrees.headings['left_heading'])))

        # Collision check with Right Paddle
        if -720 <= ball_x <= -700 and (
                right_paddle + PADDLE_HEIGHT / 2 >= ball_y >= right_paddle - PADDLE_HEIGHT / 2):
            self.ball.setheading(self.ball.towards(random.choice(degrees.headings['right_heading'])))