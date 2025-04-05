import turtle

def hexagon(size):
    for _ in range(6):
        turtle.forward(size)
        turtle.right(60)

def radial(len, count):
    for _ in range(count):
        hexagon(len)
        turtle.right(360 / count)

turtle.speed(0.5)
radial(50, 10)

turtle.done()

