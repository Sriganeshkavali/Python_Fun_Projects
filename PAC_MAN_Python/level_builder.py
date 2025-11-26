from turtle import Turtle
from configuration import GRID_SIZE, LEVEL_MAP

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.walls = []  # List of (x, y) coordinates for walls
        self.foods = []  # List of food turtles
        self.hideturtle()
        self.penup()
        self.speed("fastest")

    def setup_maze(self):
        # Calculate offset to center the maze on screen
        start_x = -((len(LEVEL_MAP[0]) * GRID_SIZE) / 2)
        start_y = ((len(LEVEL_MAP) * GRID_SIZE) / 2)

        for r, row in enumerate(LEVEL_MAP):
            for c, char in enumerate(row):
                screen_x = start_x + (c * GRID_SIZE)
                screen_y = start_y - (r * GRID_SIZE)

                if char == "X":
                    self.create_wall(screen_x, screen_y)
                elif char == ".":
                    self.create_food(screen_x, screen_y)
                
        return start_x, start_y

    def create_wall(self, x, y):
        # We draw a square stamp for a wall
        self.goto(x, y)
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=GRID_SIZE/20, stretch_len=GRID_SIZE/20)
        self.stamp()
        self.walls.append((round(x), round(y)))

    def create_food(self, x, y):
        f = Turtle()
        f.shape("circle")
        f.color("white")
        f.shapesize(0.25, 0.25) # Small dot
        f.penup()
        f.goto(x, y)
        self.foods.append(f)

    def destroy_food(self, food_turtle):
        food_turtle.goto(1000, 1000) # Move off screen
        food_turtle.hideturtle()
        self.foods.remove(food_turtle)