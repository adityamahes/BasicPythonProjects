import turtle
import pandas

screen = turtle.Screen(); screen.title("US States Game"); image = "blank_states_img.gif"; screen.addshape(image)
bg_turtle = turtle.Turtle(); bg_turtle.shape(image)
drawer = turtle.Turtle(); drawer.penup(); drawer.hideturtle()
scoreboard = turtle.Turtle(); scoreboard.hideturtle(); scoreboard.penup(); scoreboard.goto(0, 250)
guessed = []

while len(guessed) < 50:
    scoreboard.clear()
    scoreboard.write(arg=f"Score: {len(guessed)}/50", align="center", font=("Courier", 20, "bold"))
    answer_state = screen.textinput(title="Guess the state", prompt="What is the name of another state?").title()
    data = pandas.read_csv("50_states.csv")
    all_states = data.state.tolist()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed]
        csv = pandas.DataFrame(missing_states).to_csv("To_Learn.csv")
        break
    if answer_state in all_states and answer_state not in guessed:
        state = data[data.state == answer_state]
        drawer.goto(state.x.item(), state.y.item())
        drawer.write(answer_state, align="center")
        guessed.append(answer_state)
# States to learn

