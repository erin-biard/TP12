import turtle

def drawCurve(turtle,L, n):
    if n == 0:
        return turtle.forward(L)

    else:
        drawCurve(turtle,L/3,n-1)
        turtle.left(60)
        drawCurve(turtle,L/3,n-1)
        turtle.right(120)
        drawCurve(turtle,L/3,n-1)
        turtle.left(60)
        drawCurve(turtle,L/3,n-1)

def drawFullCurve(turtle,L,n):
    turtle.penup()
    turtle.goto(-400+1.5*L,0)
    turtle.pendown()
    for i in range(3):
        drawCurve(turtle,L,n)
        turtle.right(120)

turtle.setup(800,400)
turtle.hideturtle()
drawFullCurve(turtle,200,2)
turtle.exitonclick()
