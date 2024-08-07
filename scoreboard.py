from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.show_level()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT)

    def show_level(self):
        self.clear()
        self.goto(-250, 250)
        self.write(f'Score: {self.score}', align='left', font=FONT)

    def level_up(self):
        self.score += 1
        self.show_level()
        
