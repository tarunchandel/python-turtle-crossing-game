from turtle import Turtle
import utils

HEIGHT = 600
WIDTH = 800
CAR_BOUND_XCOR = WIDTH / 2 - 20


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.shape("square")
        self.color(utils.random_color())
        self.setup()

    def setup(self):
        xcor = utils.random_xcor()
        ycor = utils.random_ycor()
        if ycor < 0:
            self.setheading(180)
        else:
            self.setheading(0)
        self.goto(xcor, ycor)

    def move(self):
        if self.heading() == 180 and self.xcor() > -CAR_BOUND_XCOR:
            self.forward(10)
        elif self.heading() == 0 and self.xcor() < CAR_BOUND_XCOR:
            self.forward(10)
        else:
            self.restart()

    def restart(self):
        if self.heading() == 180:
            self.goto(CAR_BOUND_XCOR, -abs(utils.random_ycor()))

        elif self.heading() == 0:
            self.goto(-CAR_BOUND_XCOR, abs(utils.random_ycor()))
