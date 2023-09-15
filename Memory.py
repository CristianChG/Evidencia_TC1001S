"""Memory, puzzle game of number pairs."""
# import each function used from the turtle and random libraries

from random import shuffle
from turtle import up
from turtle import update
from turtle import down
from turtle import goto
from turtle import color
from turtle import begin_fill
from turtle import end_fill
from turtle import left
from turtle import forward
from turtle import clear
from turtle import shape
from turtle import stamp
from turtle import setup
from turtle import done
from turtle import onscreenclick
from turtle import tracer
from turtle import hideturtle
from turtle import addshape
from turtle import ontimer
from turtle import write

from freegames import path

car = path('car.gif')  # load the image in "car"
tiles = list(range(32)) * 2  # list to control the 32 pairs
state = {'mark': None}  # state to detect when a tile is mark
hide = [True] * 64  # The game starts with the tiles hidden.
taps = 0  # This variable counts the number of taps
matched = 0  # This variable counts the number of pairs matched


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global taps  # designate taps as a global variable in this function
    global matched  # designate matched as a global variable in this function
    taps += 1  # increase the value of taps when the program detects a click
    print(taps, "taps have occurred")  # print the number of current taps
    # calculate the index of the tile based on the coordinates clicked
    spot = index(x, y)
    mark = state['mark']

    # Detect when the tiles doesn't match or when you haven't opened a pair yet
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot  # show the tile that is currently selected
    else:
        hide[spot] = False  # show the pair found
        hide[mark] = False
        state['mark'] = None  # restart the selection
        # increase the value of "matched" when the the user finds a pair
        matched += 1

    # Check if all pairs have been matched
    if matched == 32:
        print("You have solved this puzzle!")
        # Print a final message at the end of the game
        print(taps, "taps occurred")


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:  # check if each tile is hidden
            x, y = xy(count)
            square(x, y)  # a white square is drawn in the tile

    mark = state['mark']

    # display the value of the player's selected tile if that tile is hidden.
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    # updates to show the changes you made every 100 ms
    update()
    ontimer(draw, 100)


shuffle(tiles)  # mix the tiles randomly
# defines the size and initial position of the window
setup(420, 420, 370, 0)
addshape(car)  # use the car.gif image for the game
hideturtle()
tracer(False)
onscreenclick(tap)  # detect click
draw()  # draw and update the game viewport
done()
