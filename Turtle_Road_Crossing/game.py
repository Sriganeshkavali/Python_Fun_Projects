import time
from turtle import Screen
from player import Player
from car import CarManager
from scoreboard import Scoreboard

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0) # Turns off automatic animation for smoother manual updates
screen.title("Turtle Crossing Game")

# Initialize Objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Event Listeners
screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_is_on = True
while game_is_on:
    # Screen refresh rate
    time.sleep(0.1)
    screen.update()

    # 1. Create and Move Cars
    car_manager.create_car()
    car_manager.move_cars()

    # 2. Detect collision with car
    for car in car_manager.all_cars:
        # If the distance between turtle and car is less than 20 pixels
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # 3. Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()