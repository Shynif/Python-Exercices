import turtle as t

t.down()

def spirale(n, l, s):
    t.speed(s)
    for i in range (n) :
        angle = 360/(i+3)
        t.forward(l)
        t.left(angle)

spirale(150, 20, 10)

input("attend la fin")