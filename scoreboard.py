from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Consolas', 15, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        with open("data.txt", "r") as score_data:
            self.high_score = int(score_data.read())
        self.color("white")
        self.hideturtle()
        self.setposition(0, 270)

    def increase_score(self):
        self.count += 1

    def reset(self):
        if self.count > self.high_score:
            self.high_score = self.count
            with open("data.txt", "w") as score_data:
                score_data.write(str(self.count))
        self.count = 0
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"score = {self.count} High Score = {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over🚩", align=ALIGNMENT, font=FONT)
