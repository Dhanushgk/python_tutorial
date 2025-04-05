import turtle

def star(length):
    for _ in range(5):
        turtle.forward(length)
        turtle.right(144)

star(100)
turtle.done()
