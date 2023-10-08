from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.setposition(0, 160)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.l_score}   {self.r_score}", align='center', font=('Courier', 50, 'bold'))

    def update_l_score(self):
        self.l_score += 1
        self.update_score()

    def update_r_score(self):
        self.r_score += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.setposition(0, 0)
        if self.l_score > self.r_score:
            self.write(f"Left Player Win", align='center', font=('Courier', 50, 'bold'))
        else:
            self.write(f"Right Player Win", align='center', font=('Courier', 50, 'bold'))

