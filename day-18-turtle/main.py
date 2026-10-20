from turtle import Turtle, Screen, colormode
import random

colours = colormode(255)
directions = [0, 90, 180, 270]

screen = Screen()
is_race = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="which turtle will win the race? Enter a color:"
)
print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
pos_y = [20, 50, 80, -20, -80, -50]
pos_x = -245
all_turtles = []
for index_t in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[index_t])
    new_turtle.goto(pos_x, pos_y[index_t])
    all_turtles.append(new_turtle)

if user_bet:
    is_race = True

while is_race:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You I'v won {winning_color}")
            else:
                print(f"You I'v lost! {winning_color}")

        ran_dis = random.randint(0, 10)
        turtle.forward(ran_dis)


print(all_turtles)
#
# def color_mode():
#     r = random.randint(0,255)
#     b = random.randint(0,255)
#     g = random.randint(0,255)
#     return (r, b, g)
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.left(angle)
#
#
# def random_walk(num):
#     for _ in range(num):
#         timmy.color(color_mode())
#         timmy.forward(30)
#         timmy.setheading(random.choice(directions))
#
#
# def circle_mode(size_of_gap):
#     for num_sides in range(int(360/size_of_gap)):
#         timmy.color(color_mode())
#         timmy.circle(100)
#         timmy.setheading(timmy.heading()+ size_of_gap)
#
#


def sum_to_loop(n):
    total = 0
    for num in range(n + 1):
        total += num


screen.exitonclick()
