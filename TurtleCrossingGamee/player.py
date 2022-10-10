from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("black")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def back_to_start(self):
        self.goto(STARTING_POSITION)

    def move_up(self):
        x = self.xcor()
        y = self.ycor() + MOVE_DISTANCE
        self.goto(x, y)

    def is_at_finish(self):
        return self.ycor() >= FINISH_LINE_Y
