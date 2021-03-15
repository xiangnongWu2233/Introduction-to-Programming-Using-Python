def levy(n):
    if n==0:
        return 'F'
    pre=levy(n-1)
    now=''
    for i in range(len(pre)):
        if pre[i]=='F':
            now+='L'
            now+='F'
            now+='R'
            now+='F'
            now+='L'
        else:
            now+=pre[i]
    return now
            

def drawLevy(n):
    import turtle
    from math import sqrt
    s=turtle.Screen()
    t=turtle.Turtle()
    t.penup()
    t.goto(-100,0)
    t.pendown()
    t.speed(10)
    command=levy(n)
    for i in command:
        if i=='L':
            t.left(45)
        if i=='R':
            t.right(90)
        if i=='F':
            t.forward(200*(sqrt(2)/2)**n)
    t.hideturtle()
