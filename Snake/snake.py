from turtle import *
from random import randrange
from freegames import square, vector

# The initial position of the food item is defined randomly
foodX = randrange(-15, 15) * 10
foodY = randrange(-15, 15) * 10
food = vector(foodX, foodY)
#Establishes initial position for the snake and its direction
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def colorBody():
    "Randomizes a color in a selection of 5 for the snake's body and the food item at the start of every game"
    color = randrange(1,6)
    if color == 1:
        colorString = 'black'
    elif color == 2:
        colorString = 'blue'
    elif color == 3:
        colorString = 'green'
    elif color == 4:
        colorString = 'violet'
    elif color == 5:
        colorString = 'brown'
    return colorString

colorB = colorBody()
colorF = colorBody()
#Makes sure the colors of the game elements dont match
while colorF == colorB:
    colorF = colorBody()

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    "If the snake encounters a border or itself, it turns read and dies, ending the game"
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    "If the head touches a food item, it grows and the food item appears randomly in a different position"
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    "Turns the body of the snake into the appropriate color"
    for body in snake:
        square(body.x, body.y, 9, colorB)

    "Establishes the coordinates and color fo the food items"
    square(food.x, food.y, 9, colorF)
    update()
    ontimer(move, 100)

# Declares all the necessary specifications of the game, like the size of the window,
#the key binds that stablish the direction of the snakes movement and calls for the move function.
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
