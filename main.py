from turtle import Screen
from player import Player
from car import Car
from level import Level
import time

HEIGHT = 600
WIDTH = 800
PLAYER_BOUND_YCOR = HEIGHT / 2 - 20

screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(height=HEIGHT, width=WIDTH)
screen.colormode(255)
screen.bgpic("road.gif")
screen.tracer(0)

player = Player()
cars = []

for _ in range(10):
    car = Car()
    cars.append(car)
level = Level()
screen.listen()
screen.onkey(player.move, "Up")

game_on = True
sleep = 0.1
while game_on:
    for car in cars:
        car.move()
        if car.distance(player) <= 20:
            player.color("red")
            game_on = False

    if player.ycor() == PLAYER_BOUND_YCOR:
        player.forward(10)
        level.up()
        sleep = sleep / 1.1 ** level.level
    time.sleep(sleep)
    screen.update()

level.game_over()

# TODO 4: Create Lanes or add a background pic

screen.exitonclick()
