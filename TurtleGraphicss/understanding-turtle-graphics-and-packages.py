from turtle import Turtle, Screen, colormode  # importing Turtle and Screen clas
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tup = (r, g, b)
    return tup


class MyTurtle:
    def __init__(self, color_value, shape, color, speed, size):
        colormode(color_value)
        self.tim = Turtle()
        self.tim.shape(shape)
        self.tim.color(color)
        self.tim.speed(speed)
        self.tim.pensize(size)

    def draw_random_walk(self, points):
        self.tim.pendown()
        directions = []
        for _ in range(1, points + 1):
            directions.append(_)
        for i in range(3, 1000):
            self.tim.color(random_color())
            self.tim.right(random.choice(directions)*360/points)
            self.tim.forward(30)

    def draw_spirograph(self, points):
        self.tim.pendown()
        for _ in range(points):
            self.tim.color(random_color())
            self.tim.circle(100)
            self.tim.right(360/points)


tim = MyTurtle(255, "arrow", "red", "fastest", "15")
tim.draw_random_walk(80)

screen = Screen()
screen.exitonclick()
