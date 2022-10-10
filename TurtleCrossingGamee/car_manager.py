from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, level):
        super().__init__()
        self.create()
        self.move_speed = STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * level)

    def create(self):
        self.shape("square")
        self.penup()
        self.shapesize(2, 1)
        self.goto(300, random.randint(-230, 230))
        self.color(random.choice(COLORS))
        self.setheading(90)

    def move(self):
        x = self.xcor() - self.move_speed
        y = self.ycor()
        self.goto(x, y)

    def increment_speed(self):
        self.move_speed += MOVE_INCREMENT
