from turtle import Turtle

HEIGHT = 600
WIDTH = 800
LEVEL_XCOR = WIDTH / 2 - 60
LEVEL_YCOR = HEIGHT / 2 - 40


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level: int = 0
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.goto(-LEVEL_XCOR, LEVEL_YCOR)
        self.print_level()

    def up(self):
        self.level += 1
        self.print_level()

    def print_level(self):
        self.clear()
        self.write(f"Level: {self.level}", move=False, align='center', font=('Arial', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"G   A   M   E       O   V   E   R \nBe careful while crossing the road",
                   move=False, align='center', font=('Courier', 20, 'normal'))
