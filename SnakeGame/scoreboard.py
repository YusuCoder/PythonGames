from os import write
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 280)
        self.color("white")
        self.hideturtle()
        self.score = -1
        self.update_score()

    def write_score(self):
        self.clear()
        self.write(f'Score = {self.score}', align='center', font=("Courier", 10, "normal"))

    def update_score(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f'GAME OVER\nScore: {self.score}', align='center', font=("Courier", 20, "normal"))
