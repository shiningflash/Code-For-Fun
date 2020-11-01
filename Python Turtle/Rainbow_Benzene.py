import turtle

screen = turtle.Screen()
screen.bgcolor('black')
turtle.speed(.00005)

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

alex = turtle.Pen()

for x in range(360):
    alex.pencolor(colors[x%6])
    alex.width(x/100 + 1)
    alex.forward(x)
    alex.left(59)

screen.exitonclick()