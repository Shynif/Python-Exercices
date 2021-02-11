import turtle as t

t.speed(100)

def circle(n, d):
    for i in range (n) :
        t.forward(d)
        t.left(360/n)

for i in range(360) :
    circle(i, 5)

input("finit")
