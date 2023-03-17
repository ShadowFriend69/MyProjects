from turtle import Turtle
STARING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.goto(STARING_POSITION)
        self.setheading(90)

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def new_level(self):
        # self.clear()
        self.goto(STARING_POSITION)
