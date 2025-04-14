import csv, pandas, turtle

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="What's the state?", prompt="Guess another state's name:")
print(answer_state)

screen.exitonclick()