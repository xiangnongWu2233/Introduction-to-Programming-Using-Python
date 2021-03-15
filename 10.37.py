def move(turtle, x, y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

    
def square(turtle, x, y, size):

    turtle.setheading(90)
    dis=int(size/2)
    move(turtle, x+dis,y)
    turtle.forward(dis)
    for i in range(3):
        turtle.left(90)
        turtle.forward(2*dis)
    turtle.left(90)
    turtle.forward(dis)

def squares(n, turtle, x, y, size):

    if n==1:
        square(turtle, x,y, size)

    else:
        dis=int(size/2)

        square(turtle, x, y, size)

        squares(n-1,turtle, x-dis, y-dis, dis)
        squares(n-1,turtle, x-dis, y+dis, dis)
        squares(n-1,turtle, x+dis, y-dis, dis)
        squares(n-1,turtle, x+dis, y+dis, dis)
    
'''from turtle import Screen, Turtle
s= Screen()
t= Turtle()'''

