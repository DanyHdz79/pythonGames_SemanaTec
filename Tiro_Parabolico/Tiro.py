"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.

"""

from random import randrange
from turtle import *
from freegames import vector

#Establishes the space allowed for the ball to move on screen
ball = vector(-200, -200)
#Initializes a vector where the speed values will be stored
speed = vector(0, 0)
#Creates a list where the targets will be stored
targets = []

def tap(x, y):
    "Respond to screen tap."
    "In case the ball is not currently on a 'shot'"
    if not inside(ball):
        "Sets the ball position to the left bottom of the window"
        ball.x = -199
        ball.y = -199
        "Establishes the speed values of the ball at each position"
        speed.x = (x + 200) / 15
        speed.y = (y + 200) / 15

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        "Determines the position on the screen where the target will be drawn"
        goto(target.x, target.y)
        "Especifies the size and color of the target"
        dot(20, 'blue')

    if inside(ball):
        "Determines the position on the screen where the ball will be drawn"
        goto(ball.x, ball.y)
        "Especifies the size and color of the ball"
        dot(6, 'red')
    "Perform a TurtleScreen update"
    update()

def move():
    "Move ball and targets."
    "Just in case the random number within 40 posibilities returns number zero (0)"
    if randrange(40) == 0:
        "Determines the 'y' position of the target through a random number between -150 and 150"
        y = randrange(-150, 150)
        "Establishes the initial position of the target at the right side of the screen and at the 'y' height"
        target = vector(200, y)
        "Adds the new item to the list of targets"
        targets.append(target)

    for target in targets:
        "Sets the target's 'x' value, moving the item two units to the left"
        target.x -= 2

    if inside(ball):
        "Sets the ball's 'y' speed value, moving the item 0.8 units down and creating a 'projectile motion'"
        speed.y -= 0.8
        "Calls the ball to move with the actual speed values"
        ball.move(speed)

    "Copies the actual list of targets"
    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    "Calls the ball and the targets to be drawn"
    draw()

    "For each target in the list..."
    for target in targets:
        "Checks if any target left the screen"
        if not inside(target):
            "We restablish the position of the target within the screen"
            y = randrange(-150, 150)
            target.x = 200
            target.y = y

    "Install a timer that calls the 'move' function after 50 milliseconds"
    ontimer(move, 50)

#Initializes the game setup and the specifies of the window
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
