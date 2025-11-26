import time
from turtle import Screen, Turtle
from configuration import *
from level_builder import Level
from characters import Pacman, Ghost

# 1. Setup Screen
screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor(BACKGROUND_COLOR)
screen.title("Turtle Pac-Man")
screen.tracer(0) # Turn off animation for speed

# 2. Setup Level & Maze
level = Level()
start_x_offset, start_y_offset = level.setup_maze()

# 3. Create Characters
player = Pacman()
ghosts = []
ghost_colors = ["red", "pink", "cyan", "orange"]

# Find start positions from map
for r, row in enumerate(LEVEL_MAP):
    for c, char in enumerate(row):
        screen_x = start_x_offset + (c * GRID_SIZE)
        screen_y = start_y_offset - (r * GRID_SIZE)
        
        if char == "P":
            player.goto(screen_x, screen_y)
        elif char == "G":
            # Assign color cyclically
            color = ghost_colors[len(ghosts) % len(ghost_colors)]
            new_ghost = Ghost(color, screen_x, screen_y)
            ghosts.append(new_ghost)

# 4. Keyboard Bindings
screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")

# Score Writer
score_pen = Turtle()
score_pen.hideturtle()
score_pen.penup()
score_pen.color("white")
score_pen.goto(0, HEIGHT/2 - 40)
score = 0
score_pen.write(f"Score: {score}", align="center", font=("Arial", 24, "bold"))

# 5. Game Loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(REFRESH_RATE)

    # Move Player
    player.move(level.walls)

    # Move Ghosts
    for ghost in ghosts:
        ghost.move_randomly(level.walls)
        
        # Collision with Ghost
        if player.distance(ghost) < GRID_SIZE / 2:
            score_pen.goto(0, 0)
            score_pen.write("GAME OVER", align="center", font=("Arial", 30, "bold"))
            game_is_on = False

    # Eat Food
    for food in level.foods:
        if player.distance(food) < GRID_SIZE / 2:
            level.destroy_food(food)
            score += 10
            score_pen.clear()
            score_pen.write(f"Score: {score}", align="center", font=("Arial", 24, "bold"))

    # Check Win Condition
    if len(level.foods) == 0:
        score_pen.goto(0, 0)
        score_pen.write("YOU WIN!", align="center", font=("Arial", 30, "bold"))
        game_is_on = False

screen.exitonclick()