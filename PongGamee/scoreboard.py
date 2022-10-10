from turtle import Turtle
FONT = ("square", 60, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.initialize()
        self.r_score = 0
        self.l_score = 0
        self.update()

    def initialize(self):
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.goto(0, 400)
        while self.ycor() > -400:
            self.setheading(90)
            self.penup()
            self.forward(10)
            self.pendown()
            self.forward(10)

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update()

    def r_point(self):
        self.r_score += 1
        self.update()
