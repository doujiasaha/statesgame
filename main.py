import csv
import pandas
import turtle

#create screen and set bg to a picture of the states
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#create turtle that writes the state on correct prompt
statewriter = turtle.Turtle()
statewriter.hideturtle()
statewriter.penup()
#load data from csv with pandas
data = pandas.read_csv("50_states.csv")

counter = 0
deathcounter = 3
duplicates = []
answer_state = screen.textinput(title="What's the state? {deathcounter} life left.", prompt="Guess another state's name:").title()

game_is_on = True
while game_is_on:
 

 
    #create new dict that saves key from correct value
    matching_keys = [k for k, v in data['state'].items() if v.title() == answer_state.title()]


    if answer_state == "Exit":
        
        remaining_states = pandas.DataFrame({
            "Remaining States": [value for k, value in data['state'].items() if value not in duplicates]
        })
        remaining_states.to_csv("remaining_states.csv", index_label="Index")
        
        break
    #if dict is filled grab x and y cords from df. Let turtle write it
    if matching_keys:
        duplicates.append(data['state'][matching_keys[0]])
        key = matching_keys[0]
        x_coord = data['x'][key]
        y_coord = data['y'][key]
        statewriter.goto(x_coord,y_coord)
        statewriter.write(f"{answer_state}")
        counter += 1
    else:
        deathcounter -= 1

    if deathcounter == 0:
        statewriter.goto(0,0)
        statewriter.write("GAME OVER")
        game_is_on = False
    elif counter == 50:
        statewriter.goto(0,0)
        statewriter.write("YOU'VE GUESSED ALL STATES. YOU WON!")
        game_is_on = False
    else:
        answer_state = screen.textinput(title=f"{counter}/50 guessed so far. {deathcounter} life left.", prompt="Guess another state's name:").title()
        
        if answer_state in duplicates:
            answer_state = screen.textinput(title=f"{counter}/50 guessed so far. {deathcounter} life left.", prompt=f"{answer_state} has already been guessed.").title()

    
