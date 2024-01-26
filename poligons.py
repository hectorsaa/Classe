import turtle
tortuga=turtle.Turtle()
tortuga.pensize(5)
tortuga.speed(10)

def poligon_regular(costats):
    angle=360/costats
    for i in range(costats):
        tortuga.forward(50)
        tortuga.left(angle)


poligon_regular(4)
tortuga.penup()
tortuga.goto(-150,0)
tortuga.pendown()
poligon_regular(5)
tortuga.penup()
tortuga.goto(0,100)
tortuga.pendown()
poligon_regular(6)
tortuga.penup()
tortuga.goto(150,0)
tortuga.pendown()
poligon_regular(7)

turtle.done()