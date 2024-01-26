import turtle

tortuga=turtle.Turtle()
tortuga.pensize(5)
tortuga.speed(0)
tortuga.goto(-600,0)

def estrella():
    tortuga.color("orange")  
    tortuga.begin_fill()
    for i in range(5):
        tortuga.forward(400)
        tortuga.right(144)
    tortuga.end_fill()
    tortuga.penup()  
    tortuga.forward(400)
    tortuga.pendown()

for i in range(3):
    estrella()

turtle.done()