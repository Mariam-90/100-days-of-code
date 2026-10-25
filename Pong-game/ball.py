from turtle import  Turtle
import random
Y_POSITIONS = [10,20,50, 300,200, 70,90,150]
X_POSITIONS = [-10,-20,-50, -300,-200, -70,-90,-150]
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.create_circle()

    def create_circle(self):
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(0,0)

    def move(self):
        new_x = self.xcor() +  self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)


    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1
