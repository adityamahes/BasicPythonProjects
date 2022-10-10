from turtle import Turtle, Screen
class Paddle(Turtle):
    def __init__(self, side):
        self.side = side
        super().__init__()
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        if self.side == "left":
            self.goto(-350, 0)
        if self.side == "right":
            self.goto(350, 0)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)




