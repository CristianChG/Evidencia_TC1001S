# Evidencia_TC1001S
Original Code
The original code is a simple implementation of the Tic Tac Toe game. It uses the turtle module to draw the grid and the freegames module to draw the X and O markers. The game state is stored in a dictionary, with the 'player' key indicating the current player and the 'board' key storing the current state of the board.

Modified Code
The modified code makes the following changes to the original code:

The X and O markers are now drawn in different colors.
The tap() function now checks if the square on the board is empty before drawing the X or O marker.
The grid() function now uses a smaller grid size, which makes the game easier to play.
The setup() function now sets the window title to "Tic Tac Toe".
How to Run the Code
To run the code, you will need to install the turtle and freegames modules. You can do this by running the following commands in your terminal:

pip install turtle
pip install freegames
Once you have installed the modules, you can run the code by typing the following command in your terminal:

python tic_tac_toe.py
How to Play the Game
The game is played by two players, who take turns placing their X or O marker in an empty square on the board. The first player to get three of their markers in a row, either horizontally, vertically, or diagonally, wins the game. If all nine squares are filled and no player has three of their markers in a row, the game is a draw.
