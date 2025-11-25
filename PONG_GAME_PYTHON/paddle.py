import turtle

class Paddle(turtle.Turtle):
    """
    Represents a paddle object.
    (In a multi-file setup, this class would be in 'paddle.py')
    """
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1) # Makes it 20x100 pixels
        self.penup()
        self.goto(position)
        self.speed_factor = 20 # Movement step size

    def go_up(self):
        """Moves the paddle up, checking for boundaries."""
        new_y = self.ycor() + self.speed_factor
        if new_y < 250:
            self.sety(new_y)

    def go_down(self):
        """Moves the paddle down, checking for boundaries."""
        new_y = self.ycor() - self.speed_factor
        if new_y > -250:
            self.sety(new_y)