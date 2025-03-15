from turtle import Turtle
MOVEMENT_SPEED = 40

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddles = []
        self.positions = [(720.0, 0), (-720.0, 0)]


    def paddle(self):
        for i in range(2):
            paddls = Turtle("square")
            paddls.penup()
            paddls.color("white")
            self.paddles.append(paddls)
            paddls.shapesize(stretch_wid=5.5, stretch_len=1.5)
            self.paddles[i].goto(self.positions[i])



    def move_up_left_paddle(self):
        new_y_pos = self.paddles[0].ycor() + MOVEMENT_SPEED
        if new_y_pos < 380:
            self.paddles[0].sety(new_y_pos)

    def move_down_left_paddle(self):
        new_y_pos = self.paddles[0].ycor() - MOVEMENT_SPEED
        if new_y_pos > -380:
            self.paddles[0].sety(new_y_pos)

    def move_up_right_paddle(self):
        new_y_pos = self.paddles[1].ycor() + MOVEMENT_SPEED
        if new_y_pos < 380:
            self.paddles[1].sety(new_y_pos)

    def move_down_right_paddle(self):
        new_y_pos = self.paddles[1].ycor() - MOVEMENT_SPEED
        if new_y_pos > -380:
            self.paddles[1].sety(new_y_pos)