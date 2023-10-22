from turtle import Turtle
STARTING_POSITION = (0, -280)
DISTANCE = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('seagreen')
        self.penup()
        self.seth(90)
        self.goto(STARTING_POSITION)

    def move_forwards(self):
        self.forward(DISTANCE)

    def restart(self):
        self.goto(STARTING_POSITION)
