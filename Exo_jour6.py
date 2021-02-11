import turtle as t

def fibo(n) :
    u = 0
    v = 1
    f = [] # fibonacci
    for i in range(n) :
        s = u
        u = u + v
        v = s
        f.append(u)
    return f

l = fibo(100)

t.down()
t.forward(20)
for i in l :
    r = i%10
    if (r != 0):
        if (r%2 == 0) :
            t.right(90)
        else :
            t.left(90)
        t.forward(20)

input("finit")