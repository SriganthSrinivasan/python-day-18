#Exploring Turtle Program to use its options
# from turtle import Turtle, Screen
#
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

import heroes
print(heroes.gen(5))