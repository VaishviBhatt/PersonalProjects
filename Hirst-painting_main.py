import turtle

import colorgram
from turtle import Turtle
import random

# colors_extracted = []
# colors = colorgram.extract("hirst painting.jpeg", 30)
# for color in colors:
  #  red = color.rgb.r
   # green = color.rgb.g
    # blue = color.rgb.b
    # new_color = (red, green, blue)
    # colors_extracted.append(new_color)

timmy = Turtle()
timmy.hideturtle()
timmy.speed(20)

turtle.colormode(255)
colors = [(212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12), (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187), (151, 206, 220)]
# Make the empty space around the painting
timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
timmy.pendown()


number_of_dots = 101

def ten_dots():
    for dot_count in range(1, number_of_dots):
        timmy.pensize(20)
        timmy.dot(20, random.choice(colors))
        timmy.penup()
        timmy.forward(50)

        if dot_count % 10 == 0:
            timmy.setheading(90)  # turn left
            timmy.forward(50)
            timmy.setheading(180)
            timmy.forward(500)
            timmy.setheading(360)



ten_dots()

my_screen = turtle.Screen()
my_screen.exitonclick()
