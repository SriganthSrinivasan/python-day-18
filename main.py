#Creating Hirst painting using Turtle 10 x 10 art
import random
import turtle
from turtle import Turtle as t, Screen
turtle.colormode(255)

# Getting 10 RGB value from an image and save it as (r, g, b) tuples
# within a list
# import colorgram
# rgb_list = []
# colors = colorgram.extract("hirst.jpg", 20)
# for i in range(20):
#     red = (colors[i].rgb).r
#     green = (colors[i].rgb).g
#     blue = (colors[i].rgb).b
#     tuple_list = (red, green, blue)
#     rgb_list.append(tuple_list)
# print(rgb_list)


color_list = [(207, 160, 82), (54, 88, 130), (145, 91, 40),
              (140, 26, 49), (132, 177, 203), (158, 46, 83),
              (45, 55, 104), (169, 160, 39), (129, 189, 143),
              (83, 20, 44), (37, 43, 67), (186, 94, 107),
              (187, 140, 170), (85, 120, 180), (59, 39, 31)]

karuppi = t()
screen = Screen()
screen.bgcolor("black")
karuppi.shape("arrow")
karuppi.shapesize(0.25, 0.25, 0.10)
karuppi.speed(0)

# My Solution for 10 x 10 art
# x_pos = 0
# y_pos = 0
# for vertical in range(10):
#     karuppi.setx(x_pos)
#     karuppi.sety(y_pos)
#     for horizontal in range(10):
#         karuppi.fillcolor(random.choice(color_list))
#         karuppi.begin_fill()
#         karuppi.circle(5)
#         karuppi.end_fill()
#         karuppi.penup()
#         karuppi.forward(20)
#     y_pos += 20

# Using dot() solution and making the turtle invisible
karuppi.isvisible()
x_pos = 0
y_pos = 0
for vertical in range(10):
    karuppi.setx(x_pos)
    karuppi.sety(y_pos)
    for horizontal in range(10):
        karuppi.dot(10, random.choice(color_list))
        karuppi.penup()
        karuppi.forward(20)
    y_pos += 20
screen.exitonclick()