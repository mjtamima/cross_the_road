from turtle import Turtle
import random
COLORS = ['purple', 'blue', 'grey', 'green', 'yellow', 'orange', 'red']
MOVE_DISTANCE = 5
INCREMENT = 5


class Cars:

    def __init__(self):
        self.all_cars = []
        self.speed = MOVE_DISTANCE

    def generate_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            rand_y = random.randint(-250, 250)
            car.goto(300, rand_y)
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def speed_up(self):
        self.speed += INCREMENT

