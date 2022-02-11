from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_UPDISTANCE = 10
MOVE_DOWNDISTANCE = -10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.reset_position()

    def reset_position(self):
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def up(self):
        self.forward(MOVE_UPDISTANCE)

    def down(self):
        self.forward(MOVE_DOWNDISTANCE)
