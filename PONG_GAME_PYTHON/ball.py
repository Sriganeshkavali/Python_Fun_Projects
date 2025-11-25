import turtle

class Ball(turtle.Turtle):
    """
    Represents the ball object.
    (In a multi-file setup, this class would be in 'ball.py')
    """
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(0)
        self.dx = 2 # Change in x direction per move
        self.dy = 2 # Change in y direction per move
        self.move_speed = 0.01 # Delay for game loop speed

    def move(self):
        """Moves the ball based on its current direction (dx and dy)."""
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.setx(new_x)
        self.sety(new_y)

    def bounce_y(self):
        """Reverses the vertical direction."""
        self.dy *= -1

    def bounce_x(self):
        """Reverses the horizontal direction and increases speed."""
        self.dx *= -1
        self.move_speed *= 0.95
        if self.move_speed < 0.005:
            self.move_speed = 0.005 # Cap the speed

    def reset_position(self):
        """Resets the ball to the center and reverses horizontal direction."""
        self.goto(0, 0)
        self.move_speed = 0.01 # Reset speed
        self.bounce_x()