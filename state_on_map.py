from turtle import Turtle


class StateOnMap(Turtle):

    def __init__(self, name, coord):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(coord)
        self.write(name, move=False, align='center', font=('Arial', 10, 'normal'))
