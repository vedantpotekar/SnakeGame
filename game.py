import turtle
import time
import random


delay = 0.1
score = 0
high_score = 0

wn = turtle.Screen()
wn.title("SnakeGame")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('White')
head.penup()
head.goto(0, 0)
head.direction = 'Stop'

food = turtle.Turtle()
colors = random.choice(['red', 'blue', 'green'])
shapes = random.choice(['square', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

segments = []
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
# pen.write(" SnakeGameByVedant", align='center', font=('algerian', 12, 'bold'))
pen.write(" Snake_game_by_Vedant\nScore : 0    High Score : 0", align='center', font=('bradley hand itc', 16, 'bold'))


def go_up():
    if head.direction != 'down':
        head.direction = 'up'


def go_down():
    if head.direction != 'up':
        head.direction = 'down'


def go_left():
    if head.direction != 'right':
        head.direction = 'left'


def go_right():
    if head.direction != 'left':
        head.direction = 'right'


def move():
    if head.direction == 'up':
        y=head.ycor()
        head.sety(y+20)
    if head.direction == 'down':
        y=head.ycor()
        head.sety(y-20)
    if head.direction=='left':
        x=head.xcor()
        head.setx(x-20)
    if head.direction=='right':
        x=head.xcor()
        head.setx(x+20)

wn.listen()
wn.onkeypress(go_up, 'w')
wn.onkeypress(go_down, 's')
wn.onkeypress(go_left, 'a')
wn.onkeypress(go_right, 'd')



wn.mainloop()














