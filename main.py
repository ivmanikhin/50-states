import pandas as pd
import turtle

screen = turtle.Screen()
screen.title('50 states quiz')
screen.setup(800, 600)
us_map = 'blank_states_img.gif'
screen.addshape(us_map)
turtle.shape(us_map)
states = pd.read_csv('50_states.csv')
state_names = states.state.to_list()
print(state_names)
while len(state_names) > 0:
    answer = screen.textinput('Guess the State', "What's another state's name?").capitalize()
    if answer in state_names:
        state_names.pop(state_names.index(answer))
        print(len(state_names))

turtle.mainloop()
