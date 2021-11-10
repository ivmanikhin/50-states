import pandas as pd
from PIL import Image
import turtle
from state_on_map import StateOnMap

image = Image.open('blank_states_img.gif')
print(image.size)
screen = turtle.Screen()
screen.title('50 states quiz')
screen.setup(image.size[0], image.size[1])
screen.tracer(0)
screen.bgpic('blank_states_img.gif')
states = pd.read_csv('50_states.csv')
states_on_map = []
screen.tracer(0)
screen.update()
while len(states) > 0:
    try:
        answer = screen.textinput(f'{50 - len(states)}/50 States Correct', "What's another state's name?").title()
        print(answer)
    except AttributeError:
        break
    if answer in states.state.to_list():
        states_on_map.append(StateOnMap(answer, (int(states[states.state == answer].x),
                                                 int(states[states.state == answer].y))))
        screen.update()
        states = states.drop(states[states.state == answer].index.to_list())
        print(len(states))
    if answer == 'Exit':
        break
    if len(states) == 0:
        turtle.write("You WIN!", move=False, align='center', font=('Arial', 16, 'normal'))
turtle.mainloop()
states.state.to_csv('rest_states.csv', header=False, index=False)
