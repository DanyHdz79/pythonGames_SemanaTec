from random import *
from turtle import *
from freegames import path
#Imports the image
car = path('car.gif')
#Establishes the number of tiles
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
#Establishes the two global counters
cont = 0
cont2 = 0

#The parameters and initial conditions are defined
def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    #The data is filled on the diferent tiles
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

#The different coordinates get assigned an index
def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

#The index is translated into a number
def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

#With a global counter we get the number of taps that the player does
def tap(x, y):
    global cont, cont2
    cont = cont+1
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']
    print('Taps: ', str(cont))

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:#If the number of discovered tiles is equal to 32 pairs, is indced that you have won
        cont2 = cont2 + 1
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        if (cont2 == 32):
            print ("All tiles have been revealed")

#The image in the background and the tiles are represented in a grafic way
def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()
    #Draw the tiles
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)
    #Set the tiles status
    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y + 8)
        color('black')
        write(tiles[mark], align = "center", font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)

#Shuffles the tiles randomly
shuffle(tiles)
#Establishes the setup of the game
setup(420, 420, 370, 0)
#Imports the background image
addshape(car)
hideturtle()
tracer(False)
#Registers the clicks
onscreenclick(tap)
#Draws the game
draw()
done()
