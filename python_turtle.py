import turtle

def draw_rectangle():
    """ make a rectangle """
    alex = turtle.Turtle()
    alex.pencolor('lightblue')
    alex.pensize(5)

    side1 = 150
    side2 = 80
    angle = 90

    for i in range(4):
        if i % 2 == 0:
            alex.forward(side1)
        else:
            alex.forward(side2)
        alex.left(angle)

def draw_shape1():
    """ make a shape1 """
    bob = turtle.Turtle()
    bob.pencolor('pink')
    bob.pensize(5)

    distance = 50
    angle = 90

    for _ in range(24):
        bob.forward(distance)
        bob.left(angle)
        distance += 10

def draw_shape2():
    """ make a shape2 """
    elan = turtle.Turtle()
    elan.pencolor('lightgreen')
    elan.pensize(5)

    distance = 45
    angle = 90

    for _ in range(11):
        elan.forward(distance)
        elan.left(angle)
        distance += 10
        angle -= 3

def draw_shape3():
    """ make a shape """
    """ start shape """
    tess = turtle.Turtle()
    tess.color('grey')
    tess.shape("turtle")

    dis = 5
    tess.up()

    for _ in range(34):
        tess.stamp()
        tess.forward(dis)
        tess.right(24)
        dis += 2

def draw_traingle():
    """ make a Equilateral triangle """
    arm = 200
    angle = 120

    trudy = turtle.Turtle()
    trudy.pencolor('royal blue')
    trudy.pensize(5)

    for _ in range(3):
        trudy.forward(arm)
        trudy.left(angle)

if __name__ == "__main__":
    screen = t=turtle.Screen()
    screen.bgcolor('white')
    draw_rectangle()
    draw_shape1()
    draw_shape2()
    draw_shape3()
    draw_traingle()
    screen.exitonclick()
