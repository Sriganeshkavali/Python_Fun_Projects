import turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


def draw_dividing_line():
    """Draws a dashed line down the center of the screen."""
    line_turtle = turtle.Turtle()
    line_turtle.color("white")
    line_turtle.pensize(3)
    line_turtle.hideturtle()
    line_turtle.penup()
    line_turtle.goto(0, 300)
    line_turtle.setheading(270) # Point down

    # Draw dashed line segments
    for _ in range(15):
        line_turtle.pendown()
        line_turtle.forward(20)
        line_turtle.penup()
        line_turtle.forward(20)

# Setup the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Python Turtle Pong (Refactored)")
screen.tracer(0) # Turns off screen updates for manual control

# Draw the visual partition
draw_dividing_line()

# Create game objects
paddle_a = Paddle((-350, 0)) # Left Paddle
paddle_b = Paddle((350, 0)) # Right Paddle
ball = Ball()
scoreboard = Scoreboard()

# Keyboard Bindings (Player A: W/S, Player B: Up/Down)
screen.listen()

# Player A Controls (Left Paddle)
screen.onkey(paddle_a.go_up, "w")
screen.onkey(paddle_a.go_down, "s")

# Player B Controls (Right Paddle)
screen.onkey(paddle_b.go_up, "Up")
screen.onkey(paddle_b.go_down, "Down")

# Game Loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed) # Control the game speed

    # Move the ball
    ball.move()

    # Border Checking (Top and Bottom)
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Paddle Collision (Ball hits paddle)
    # Check Right Paddle (Paddle B)
    if (ball.distance(paddle_b) < 60) and (ball.xcor() > 330):
        ball.bounce_x()

    # Check Left Paddle (Paddle A)
    if (ball.distance(paddle_a) < 60) and (ball.xcor() < -330):
        ball.bounce_x()

    # Score Checking (Ball goes out of bounds)

    # Ball passes right side (Player A scores)
    if ball.xcor() > 390:
        scoreboard.increase_score_a()
        ball.reset_position()
        paddle_a.goto(-350, 0) # Reset paddles to center
        paddle_b.goto(350, 0)


    # Ball passes left side (Player B scores)
    if ball.xcor() < -390:
        scoreboard.increase_score_b()
        ball.reset_position()
        paddle_a.goto(-350, 0) # Reset paddles to center
        paddle_b.goto(350, 0)

    # Win condition
    if scoreboard.score_a >= 10 or scoreboard.score_b >= 10:
        game_is_on = False
        scoreboard.goto(0, 0)
        winner = "Player A" if scoreboard.score_a > scoreboard.score_b else "Player B"
        scoreboard.write(f"GAME OVER! {winner} Wins!", align="center", font=("Courier", 30, "bold"))


screen.mainloop()