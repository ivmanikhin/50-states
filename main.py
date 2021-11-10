import pandas as pd
import turtle
from state_on_map import StateOnMap

screen = turtle.Screen()
screen.title('50 states quiz')
screen.setup(800, 600)
screen.tracer(0)
us_map = 'blank_states_img.gif'
screen.addshape(us_map)
turtle.shape(us_map)
states = pd.read_csv('50_states.csv')
state_names_original = states.state.to_list()
state_names = [item.lower() for item in state_names_original]
states_x = states.x.to_list()
states_y = states.y.to_list()
states_x = [int(x) for x in states_x]
states_y = [int(y) for y in states_y]
print(state_names)
states_on_map = []
screen.tracer(0)
screen.update()
while len(state_names) > 0:
    try:
        answer = screen.textinput('Guess the State', "What's another state's name?").lower()
        print(answer)
    except AttributeError:
        break
    if answer in state_names:
        state_index = state_names.index(answer)
        state_names[state_index] = ''
        states_on_map.append(StateOnMap(state_names_original[state_index], (states_x[state_index], states_y[state_index])))
        screen.update()

turtle.mainloop()
