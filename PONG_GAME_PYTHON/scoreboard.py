import turtle
class Scoreboard(turtle.Turtle):
    """
    Manages the score display for both players.
    (In a multi-file setup, this class would be in 'scoreboard.py')
    """
    def __init__(self):
        super().__init__()
        self.score_a = 0
        self.score_b = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        """Redraws the score on the screen."""
        self.clear()
        self.write(f"Player A: {self.score_a}   Player B: {self.score_b}",
                   align="center", font=("Courier", 24, "normal"))

    def increase_score_a(self):
        """Increments Player A's score and updates the display."""
        self.score_a += 1
        self.update_score()

    def increase_score_b(self):
        """Increments Player B's score and updates the display."""
        self.score_b += 1
        self.update_score()