from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 360)
        self.render_score()

    def render_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.render_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER! Your score is: {self.score}", align=ALIGNMENT, font=FONT)
