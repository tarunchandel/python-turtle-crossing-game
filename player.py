from turtle import Turtle

HEIGHT = 600
WIDTH = 800

PLAYER_BOUND_YCOR = HEIGHT / 2 - 20


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.goto(0, -PLAYER_BOUND_YCOR)

    def move(self):
        if self.ycor() < PLAYER_BOUND_YCOR:
            self.forward(20)
        else:
            self.restart()

    def restart(self):
        self.goto(0, -PLAYER_BOUND_YCOR)
