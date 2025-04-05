import turtle
def pentagon(length):
    for _ in range(5):
        turtle.forward(length)
        turtle.left(72)

pentagon(100)
turtle.done()
