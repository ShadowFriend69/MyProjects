import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
data_state_list = data.state.to_list()


def new_new_state(x, y, state):
    new_state = turtle.Turtle()
    new_state.hideturtle()
    new_state.penup()
    new_state.goto(x, y)
    new_state.write(state, align="center", font=("Arial", 8, "normal"))


guess_states = []

while len(guess_states) < 50:
    answer_state = screen.textinput(title=f"{len(guess_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        states_to_learn = [state for state in data_state_list if state not in guess_states]
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn")
        break
    if answer_state in data_state_list:
        guess_states.append(answer_state)
        state_info = data[data.state == answer_state]
        x_coor = int(state_info.x)
        y_coor = int(state_info.y)
        new_new_state(x=x_coor, y=y_coor, state=answer_state)
    else:
        print("gay")
