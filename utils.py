from random import randint

HEIGHT = 600
WIDTH = 800
XCOR_BOUND = int(round(WIDTH / 2)) - 20
YCOR_BOUND = int(round(HEIGHT / 2)) - 60


def random_color():
    return randint(0, 255), randint(0, 255), randint(0, 255)


def random_xcor():
    return randint(-XCOR_BOUND, XCOR_BOUND)


def random_ycor():
    return randint(-YCOR_BOUND, YCOR_BOUND)
