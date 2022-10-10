from turtle import Turtle, Screen, colormode
import colorgram
import random


def extract_colors(file):
    colors = colorgram.extract(file, 100)
    rgb_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb_colors.append((r, g, b))
    return rgb_colors


def make_drawing(color_list, speed):
    colormode(255)
    tim = Turtle()
    tim.penup()
    tim.speed(speed)
    tim.setheading(225); tim.forward(300); tim.setheading(0)
    for i in range(1, 100 + 1):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
        if i % 10 == 0:
            tim.left(90); tim.forward(50); tim.left(90); tim.forward(500); tim.right(180)


make_drawing(extract_colors("image.jpeg"), "fastest")

screen = Screen()
screen.exitonclick()
