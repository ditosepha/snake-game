from turtle import Turtle
with open("data.txt") as high_score_data:
    high_score = high_score_data.read()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = int(high_score)
        self.penup()
        self.hideturtle()
        self.color("white", "black")
        self.speed("fastest")
        self.goto(0, 270)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", move=False, align="center", font=('Arial', 18, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as high_score_data:
                high_score_data.write(str(self.highscore))
        self.score = 0
        self.update()

    

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align="center", font=('Arial', 18, 'normal'))
