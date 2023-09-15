"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import (
    color,
    up,
    goto,
    down,
    circle,
    setup,
    hideturtle,
    tracer,
    update,
    onscreenclick,
    done
)

from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    """Add color to X"""
    color(x_color)
    """Shrink and center the X"""
    line(x + 30, y + 30, x + 103, y + 103)
    line(x + 30, y + 103, x + 103, y + 30)


def drawo(x, y):
    """Draw O player."""
    """Add color to O"""
    color(o_color)
    up()
    goto(x + 67, y + 12)
    down()
    """Shrink the circle"""
    circle(55)


def floor(value):
    """Round value down to grid with square size 133"""
    return ((value + 200) // 133) * 133 - 200


"""Definition of the game state with the empty board"""
state = {'player': 0, 'board': [[None, None, None],
                                [None, None, None],
                                [None, None, None]]}
players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    """Check if the square on the board is empty"""
    if state['board'][int((y + 200) // 133)][int((x + 200) // 133)] is None:
        draw = players[player]
        draw(x, y)
        update()
        """Update the board with the player's move"""
        state['board'][int((y + 200) // 133)][int((x + 200) // 133)] = player
        state['player'] = not player


"""Define the colors of the X and O"""
x_color = "red"
o_color = "blue"

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
