# Python_Fun_Projects
This is my Fun Time Projects Using Python and different libraries
## Python Snake Game

* This is a classic Snake game built entirely in Python using the built-in turtle module for the graphics and game logic.

How It's Made

The project is broken down into four main Python files, each handling a different part of the game:

1. main.py: This is the main file that runs the game. It sets up the screen, creates the snake, food, and scoreboard objects, and contains the main game loop. It also listens for keyboard input (Arrow Keys) to control the snake.

2. snake.py: Defines the Snake class. This class manages all the segments of the snake's body, its movement, and the methods for changing direction (up, down, left, right).

3. food.py: Defines the Food class, which is a small blue circle. This class handles placing the food at a new random location on the screen every time the snake eats it.

4. scoreboard.py: Defines the Scoreboard class. This class is responsible for drawing the score at the top of the screen and displaying the "GAME OVER" message when the player loses.

* The game logic in main.py continuously updates the screen, moves the snake forward, and checks for two types of collisions:

1. Collision with food: If the snake's head gets close to the food, the score increases, the snake gets longer, and the food moves to a new spot.

2. Collision with wall or tail: If the snake hits the edge of the screen or runs into its own body, the game ends.

* Run the following command:

python main.py


* Play: The game window will open. Use the Up, Down, Left, and Right arrow keys to control the snake. Try to eat as much food as you can without crashing!

## Python Two-Player Pong Game

* This is a classic two-player Pong implementation built using Python's standard turtle library for graphics and user input.

### Features

* **Two-Player Local Multiplayer:** Controls for Player A (W/S) and Player B (Up/Down Arrow Keys).

* **Real-time Score Tracking:** A scoreboard at the top tracks points.

* **Dynamic Difficulty:** The ball speeds up slightly every time it hits a paddle.

* **Visual Partition:** A dashed line is drawn down the center to divide the playing field.

### Project Structure

Although provided as a single runnable file (game.py), the design follows an Object-Oriented approach, conceptually separating components into different modules:

* **scoreboard.py: ** Contains the Scoreboard class for managing and displaying scores.

* **paddle.py:** Contains the Paddle class for the player-controlled bats.

* **ball.py:** Contains the Ball class for movement and physics logic.

* **game.py:** The main runner file that sets up the screen, imports the classes, handles keyboard input, and runs the central game loop (collision detection and scoring).


**Player 1 :**
Up
Down

**Player 2** 
W
S

#### **How to Run**

Ensure you have Python installed.

Run the main file from your terminal:

python game.py


The game will open in a new window.

## Turtle Crossing Game

* A classic arcade-style game built with Python's Turtle module. Help the turtle cross the busy road without getting hit by cars!

### How to Play

Run **main.py** to start the game.

* Use Up Arrow to move forward.

* Use Down Arrow to move backward.

* Reach the top of the screen to level up.

**Avoid the cars—they get faster every level!**

#### File Structure

**main.py:** The game loop and setup.

**player.py:** Turtle movement logic.

**car_manager.py:** Car generation and movement.

**scoreboard.py: ** Level tracking and game over display.

## Turtle Pac-Man

* A simplified arcade-style Pac-Man game built using Python's standard turtle graphics module. Navigate the maze, eat all the dots, and avoid the ghosts!

### How to Play

* Start the Game: Run the run_pacman.py file.

* Controls: Use the Arrow Keys to move Pac-Man.

* Up Arrow: Move Up

* Down Arrow: Move Down

* Left Arrow: Move Left

* Right Arrow: Move Right

#### Objective: Eat all the white dots to win. If a ghost touches you, it's Game Over.

### Requirements

Python 3.x

Turtle (Standard library included with Python)

