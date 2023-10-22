from turtle import Turtle
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("green")
        self.goto(-280, 270)
        self.level = 1
        self.cur_level()

    def cur_level(self):
        self.write(arg=f"Level:{self.level}", align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.cur_level()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align="center", font=FONT)

