import turtle 

tortuga=turtle.Turtle()
tortuga.goto(0,0)
tortuga.pensize(5)
tortuga.speed(1)

def hexagon():
    for i in range(6):
        tortuga.forward(50)
        tortuga.right(60)


def triangle():
    for i in range(3):
        tortuga.forward(50)
        tortuga.left(120)

def pentagon():
    for i in range(5):
        tortuga.forward(50)
        tortuga.left(72)
triangle()
tortuga.penup()
tortuga.goto(250,50)
tortuga.pendown()
hexagon()
tortuga.penup()
tortuga.goto(50,50)
tortuga.pendown()
pentagon()

turtle.done()
