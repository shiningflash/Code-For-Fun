import turtle

screen = turtle.Screen()
turtle.speed(1)

alex = turtle.Turtle()

for i in range(100):
    alex.circle(5*i)
    alex.circle(-5*i)
    alex.left(i)

screen.exitonclick()