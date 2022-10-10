from turtle import Turtle, Screen
tim = Turtle()
tim.shape("turtle")
screen = Screen()
screen.listen() # This starts listening for user input events
# We use event listeners to bind a keystroke to an event


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.forward(-10)


def screen_clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def clockwise():
    tim.rt(10)


def counter_clockwise():
    tim.lt(10)


screen.onkeypress(key="w", fun=move_forwards)  # function as input (no parenthesis) aka Higher Order function
screen.onkeypress(key="s", fun=move_backwards)  # function as input (no parenthesis) aka Higher Order function
screen.onkeypress(key="a", fun=counter_clockwise)  # function as input (no parenthesis) aka Higher Order function
screen.onkeypress(key="d", fun=clockwise)  # function as input (no parenthesis) aka Higher Order function
screen.onkeypress(key="c", fun=screen_clear)  # function as input (no parenthesis) aka Higher Order function

screen.exitonclick()
