import turtle
my_wn = turtle.Screen()
my_wn.bgcolor("orange")
my_wn.title("turtle")
my_pen = turtle.Turtle()
size = 1
while True:
    for i in range(4):
        my_pen.fd(size + 0)
        my_pen.left(98)
        size = size - 5
    size = size + 1
