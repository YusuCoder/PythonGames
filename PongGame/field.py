from turtle import Turtle
import ball

class Field:
    def __init__(self, screen):
        self.scores = [0, 0]
        self.t = Turtle()
        self.s = screen
        self.draw_pos = [-70, 70]
        self.score = Turtle()
        self.score1 = Turtle()
        self.ball = ball
        self.lis_scores = [self.score, self.score1]

    def draw_line(self):
        self.t.width(4)
        self.t.penup()
        self.t.goto(0, 370)
        self.t.setheading(270)
        self.t.hideturtle()
        self.t.color('white')
        for i in range(25):
            self.t.pendown()
            self.t.forward(10)
            self.t.penup()
            self.t.forward(20)

    def create_scores(self):
        for i in range(2):
            self.lis_scores[i].penup()
            self.lis_scores[i].hideturtle()
            self.lis_scores[i].color('white')
            # self.lis_scores.append(self.score)
            self.lis_scores[i].goto(self.draw_pos[i], 310)
            self.lis_scores[i].write(self.scores[i], align="center", font=("OCR A Extended", 50, "bold"))

    def update_score(self):
        for i in range(2):
            self.lis_scores[i].clear()
            self.lis_scores[i].goto(self.draw_pos[i], 310)
            self.ball.SPEED = 10
            self.lis_scores[i].write(self.scores[i], align="center", font=("OCR A Extended", 50, "bold"))

