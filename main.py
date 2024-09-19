import turtle

turtle.title("Square on a Canvas")

# Screen
screen = turtle.Screen()
screen.bgcolor("Pink")

# Turtle
t = turtle.Turtle()
t.shape('classic')
t.color('white')
t.speed(1)
t.pensize(5)
t.fillcolor('blue')

t.begin_fill()
# Draw Square
for _ in range(4):
     t.forward(100)
     t.left(90)
t.end_fill()

turtle.done()