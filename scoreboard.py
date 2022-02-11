from turtle import Turtle
import turtle
ALIGNMENT = 'Left'
FONT = ("Courier", 24, "normal")
FONT2 = ("Courier", 10, "normal")
turtle.ht()
turtle.goto(0, 0)
turtle.write("Алькенов, Бондаренко, Едельбаев, Суендыков, Хандрико", align="center", font=FONT2)


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-230, 250)
        self.write(f"Level : {self.level}", move=False, align=ALIGNMENT, font=FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level : {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER ", align="center", font=FONT)

    def reset(self):
        self.clear()
        self.level = 1
        self.write(f"Level : {self.level}", align=ALIGNMENT, font=FONT)
