from turtle import Turtle
import time
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.color("Black")
        self.penup()
        self.hideturtle()

    def update_scoreboard(self, level):
        self.goto(0, 250)
        self.clear()
        self.write(arg=f"level {level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)

    def countdown(self):
        self.goto(0, 0)
        for num in range(2, -1, -1):
            self.clear()
            self.write(arg=f"{num + 1}", align="center", font=("Courier", 50, "bold"))
            time.sleep(1)