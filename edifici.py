import turtle 
tortuga=turtle.Turtle()
tortuga.pensize(5)
tortuga.speed(0)

def edifici(habitacions,pisos):
    amplada=40*habitacions
    altura=40*pisos
    for i in range(2):
        tortuga.forward(amplada)
        tortuga.left(90)
        tortuga.forward(altura)
        tortuga.left(90)
    
    for i in range(pisos):
        tortuga.pu()
        tortuga.left(90)
        tortuga.forward(10)
        tortuga.right(90)
        for i in range(habitacions):
            tortuga.forward(10)
            tortuga.pd()
            for i in range(4):
                tortuga.forward(20)
                tortuga.left(90)
            tortuga.pu()
            tortuga.forward(30)
        tortuga.backward(amplada)
        tortuga.left(90)
        tortuga.forward(30)
        tortuga.right(90)
                
            

edifici(3,5)
turtle.done()
edifici(2,2)