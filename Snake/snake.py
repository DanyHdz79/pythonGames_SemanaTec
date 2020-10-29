from turtle import *
from random import randrange
from freegames import square, vector

foodX = randrange(-15, 15) * 10
foodY = randrange(-15, 15) * 10

food = vector(foodX, foodY)
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
while colorF == colorB:
    colorF = colorBody()

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    
    for body in snake:
        square(body.x, body.y, 9, colorB)
        
    
    square(food.x, food.y, 9, colorF)
    update()
    ontimer(move, 100)

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