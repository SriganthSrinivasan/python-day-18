#Exploring Turtle Program to use its options
import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)

# karuppi = Turtle()
# vellachi = Turtle()
# screen = Screen()
# screen.screensize(3000,2000)
# screen.bgpic("space.gif")
# karuppi.shape("turtle")
# vellachi.shape("turtle")
# karuppi.shapesize(1.5, 1.5, 0.5)
# vellachi.shapesize(1.5, 1.5, 0.5)
# karuppi.color("DeepSkyBlue", "black")
# vellachi.color("DeepSkyBlue4", "white")
# karuppi.speed(1)
# vellachi.speed(1)
# vellachi.setheading(180)
# screen.textinput("Space Turtle", "Enter Username")
#
# for i in range(4):
#     karuppi.forward(100)
#     vellachi.forward(100)
#     karuppi.right(90)
#     vellachi.left(90)
#
# screen.exitonclick()

#Note: To import all the classes from a Module use *
#example: from turtle import * (Not preffered for long codes)

#Note: Its very helpful to create alias for the module
#example: from turtle import as t
#you can use t instead of turtle (turtle = t.Turtle())

#Your default python library is small with few modules
#To access whatever the modules in the world you have to install them in
#your library
# import heroes
# print(heroes.gen(5))


#Creating a dotted line using turtle penup() and pendown() methods
# karuppi = Turtle()
# screen = Screen()
# screen.screensize(3000,2000)
# screen.bgcolor("Yellow")
# karuppi.shape("turtle")
# karuppi.shapesize(1.5, 1.5, 0.5)
# karuppi.color("DeepSkyBlue", "black")
# karuppi.speed(1)
#
# for i in range(30):
#     karuppi.forward(10)
#     karuppi.penup()
#     karuppi.forward(10)
#     karuppi.pendown()
#
# screen.exitonclick()

#Drawing a Triangle, Square, Pentagon, Hexagon, Heptagon, Octagon, nonagan, decagon
#with random colors
# karuppi = Turtle()
# screen = Screen()
# screen.screensize(3000,2000)
# screen.bgcolor("black")
# karuppi.shape("turtle")
# karuppi.shapesize(1.5, 1.5, 0.5)
# color_palette = ["red", "blue", "green", "yellow", "white", "pink", "gray", "brown", "violet", "orange"]
# karuppi.color("DeepSkyBlue", "black")
# karuppi.speed(10)
# ###################################
# # def triangle():
# #     for i in range (3):
# #         karuppi.forward(100)
# #         karuppi.right(120)
# #
# # def square():
# #     for i in range (4):
# #         karuppi.forward(100)
# #         karuppi.right(90)
# #
# # def pentagon():
# #     for i in range (5):
# #         karuppi.forward(100)
# #         karuppi.right(72)
# #
# # def hexagon():
# #     for i in range (6):
# #         karuppi.forward(100)
# #         karuppi.right(60)
# #
# # def heptagon():
# #     for i in range (7):
# #         karuppi.forward(100)
# #         karuppi.right(51.43)
# #
# # def octagon():
# #     for i in range (8):
# #         karuppi.forward(100)
# #         karuppi.right(45)
# #
# # def nonagon():
# #     for i in range (9):
# #         karuppi.forward(100)
# #         karuppi.right(40)
# #
# # def decagon():
# #     for i in range (10):
# #         karuppi.forward(100)
# #         karuppi.right(36)
# #
# # triangle()
# # square()
# # pentagon()
# # hexagon()
# # heptagon()
# # octagon()
# # nonagon()
# # decagon()
# #####################################
# sides = 3
# while sides != 11:
#     karuppi.pencolor(random.choice(color_palette))
#     for i in range (sides):
#         karuppi.forward(100)
#         karuppi.right(360/sides)
#     sides += 1
#
# screen.exitonclick()



#Create a Random Walking Turtle with same distance each time before moving
#other direction with random colors each time
# karuppi = Turtle()
# screen = Screen()
# screen.screensize(3000,2000)
# screen.bgcolor("black")
# karuppi.shape("turtle")
# karuppi.shapesize(1.5, 1.5, 0.5)
# color_palette = ["red", "blue", "green", "yellow", "white", "pink", "gray", "brown", "violet", "orange"]
# karuppi.color("DeepSkyBlue", "black")
# karuppi.pensize(5)
# karuppi.speed(10)
#
# degrees_list = [0, 90, 180, 270]
# for i in range(200):
#     degree_choice = random.choice(degrees_list)
#     karuppi.pencolor(random.choice(color_palette))
#     karuppi.setheading(degree_choice)
#     karuppi.forward(10)
#
# screen.exitonclick()


#Tuple:
#Tuple is starts and end with ( & )
#Tuple is like a List but the value within tuples cant be changed (Immutable)
#It's very helpful when you want your values not to be changed by anyone
#You can convert your tuple to List using list(Your_tuple_name)


#Creating Random colors in turtle module by changing color mode to 255
# karuppi = Turtle()
# screen = Screen()
# screen.screensize(3000,2000)
# screen.bgcolor("white")
# karuppi.shape("arrow")
# karuppi.shapesize(0.75, 0.75, 0.25)
# karuppi.color("DeepSkyBlue", "black")
# karuppi.pensize(5)
# karuppi.speed(10)
# def color_mode():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rgb = (r, g, b)
#     return  rgb
#
# degrees_list = [0, 90, 180, 270]
# for i in range(200):
#     degree_choice = random.choice(degrees_list)
#     karuppi.pencolor(color_mode())
#     karuppi.setheading(degree_choice)
#     karuppi.forward(10)
#
# screen.exitonclick()



#Creating a Spirograph Circle using multiple circle and each circle must be of different color
# karuppi = Turtle()
# screen = Screen()
# screen.screensize(3000,2000)
# screen.bgcolor("black")
# karuppi.shape("arrow")
# karuppi.shapesize(0.75, 0.75, 0.25)
# karuppi.color("DeepSkyBlue", "black")
# karuppi.pensize(2)
# karuppi.speed(0)
#
# def color_mode():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rgb = (r, g, b)
#     return  rgb
#
# angle = 0
# for i in range(37):
#     karuppi.pencolor(color_mode())
#     karuppi.circle(50.0)
#     karuppi.setheading(angle)
#     angle += 10
#
# screen.exitonclick()
