from turtle import Turtle
import random
import degrees

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("purple")
        self.hit_wall = False
        self.current_direction = random.choice(degrees.directions['start'])
        self.reset_direction()

    def reset_direction(self):
        self.goto(0, 0)
        self.setheading(self.current_direction)

    def move_ball(self):
        self.speed(1)
        self.forward(10)
