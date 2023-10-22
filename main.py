from turtle import Screen
import time
from player import Player
from scoreboard import Scoreboard
from cars import Cars

screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)

timmy = Player()
scoreboard = Scoreboard()
cars = Cars()

screen.listen()
screen.onkey(timmy.move_forwards, 'Up')

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    cars.generate_car()
    cars.move ()

    for car in cars.all_cars:
        if timmy.distance(car) < 26:
            game_on = False
            scoreboard.game_over()

    if timmy.ycor() > 280:
        timmy.restart()
        scoreboard.level_up()
        cars.speed_up()

screen.exitonclick()
