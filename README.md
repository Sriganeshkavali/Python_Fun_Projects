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
