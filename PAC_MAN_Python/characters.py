from turtle import Turtle
import random
from configuration import GRID_SIZE

class Pacman(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.shapesize(stretch_wid=GRID_SIZE/24, stretch_len=GRID_SIZE/24)
        self.direction = "stop"
        self.next_direction = "stop"

    def go_up(self): self.next_direction = "up"
    def go_down(self): self.next_direction = "down"
    def go_left(self): self.next_direction = "left"
    def go_right(self): self.next_direction = "right"

    def move(self, walls):
        # Attempt to turn if requested
        if self.next_direction != "stop":
            target_x, target_y = self.get_target_coords(self.next_direction)
            if (round(target_x), round(target_y)) not in walls:
                self.direction = self.next_direction
        
        # Move in current direction if possible
        if self.direction != "stop":
            target_x, target_y = self.get_target_coords(self.direction)
            if (round(target_x), round(target_y)) not in walls:
                self.goto(target_x, target_y)
                return True # Moved successfully
        return False

    def get_target_coords(self, direction):
        x, y = self.xcor(), self.ycor()
        if direction == "up": y += GRID_SIZE
        elif direction == "down": y -= GRID_SIZE
        elif direction == "left": x -= GRID_SIZE
        elif direction == "right": x += GRID_SIZE
        return x, y

class Ghost(Turtle):
    def __init__(self, color, x, y):
        super().__init__()
        self.shape("turtle")
        self.color(color)
        self.penup()
        self.goto(x, y)
        self.speed = GRID_SIZE
        self.direction = random.choice(["up", "down", "left", "right"])

    def move_randomly(self, walls):
        # Calculate target based on current direction
        target_x, target_y = self.xcor(), self.ycor()
        
        if self.direction == "up": target_y += self.speed
        elif self.direction == "down": target_y -= self.speed
        elif self.direction == "left": target_x -= self.speed
        elif self.direction == "right": target_x += self.speed

        # If hit wall, pick new random direction, else move
        if (round(target_x), round(target_y)) in walls:
            self.direction = random.choice(["up", "down", "left", "right"])
        else:
            self.goto(target_x, target_y)