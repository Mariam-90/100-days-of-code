from turtle import  Turtle


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.position= position
        self.create_paddle(self.position)

    def create_paddle(self, position ):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        y_core = self.ycor() + 20
        self.goto(self.xcor(), y_core)

    def go_down(self):
        y_core = self.ycor() - 20
        self.goto(self.xcor(), y_core)