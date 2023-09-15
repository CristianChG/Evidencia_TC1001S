# Evidence_TC1001S
SING0401 Application of Standards and Norms

### Pacman Game Activity
We worked based on the code provided by the Grant Jenks website to subsequently test and analyze the video game code. We verified that the code follows best practices by running `python3 -m flake8 Pacman.py` in our terminal, which displayed a list of errors. Most of the errors were related to the lack of function declarations within the turtle library. To address this, we replaced the line `from turtle import *` with the names of each of the missing functions. Additionally, there was an issue with spacing between each function; we needed to add an empty space after the list of turtles where our first function is located. We ran flake8 again, and it no longer reported any errors.

We were asked to change the design of the game board, so we focused on the turtle list as it defines the board's design. Each cell on the board is represented by either 0 (an empty cell or the boundary where ghosts and Pacman can move) or 1 (points collected by Pacman). We swapped some 0s with 1s and vice versa until we achieved the desired design.

Finally, to make the ghosts move faster, we made a small adjustment to the timer in the `move()` function. Previously, it was configured as `ontimer(move, 100)`, indicating that the `move()` function was called every 100 milliseconds. To make the ghosts move faster, we reduced the timer value to 50, causing the ghosts to move twice as fast.




