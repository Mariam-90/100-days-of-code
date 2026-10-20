import colorgram
from turtle import Turtle,Screen,colormode
import random

from PIL.ImageChops import screen

# Extract 6 colors from an image.
# colors = colorgram.extract('spot.jpg', 6)
# color_list = [(245, 243, 239), (247, 242, 245), (204, 165, 107), (239, 246, 241), (237, 240, 245), (155, 73, 46)]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color =(r,g,b)
#     color_list.append(new_color)
# print(color_list)
tim = Turtle()
my_screen = Screen()
colormode(255)
tim.shape()
tim.speed(100)
color_list = [(245, 243, 239), (247, 242, 245), (204, 165, 107), (239, 246, 241), (237, 240, 245), (155, 73, 46)]

def to_do_image(number_of_dots):
    tim.setheading(225)
    tim.penup()
    tim.forward(300)
    tim.setheading(0)
    for dot_count in range(1, number_of_dots + 1):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)

        if dot_count % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)

number_of_dots = 100
def tern_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def tern_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def forwards_w():
    tim.forward(70)

def back_wards():
    tim.backward(70)
def cler_sc():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

my_screen.listen()
my_screen.onkey(forwards_w, "w")
my_screen.onkey(back_wards, "s")
my_screen.onkey(tern_left, "a")
my_screen.onkey(tern_right, "d")
my_screen.onkey(cler_sc, "c")
my_screen.exitonclick()