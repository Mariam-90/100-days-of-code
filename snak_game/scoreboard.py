from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("classic")
        self.goto(0, 280)
        self.hideturtle()
        self.score = 0
        self.add_score()

    def add_score(self):
        self.clear()
        self.write(f"Score = {self.score} ", align="center")
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over! ", align="center")