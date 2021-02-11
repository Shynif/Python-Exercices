
def fibonacci(n, a, b) :
    if (n==0) :
        return a
    elif (n == 1) :
        return b
    else :
        return fibonacci(n-1, b, a+b)

for i in range (10) :
    print(i, "------------------")
    for j in range (10) :
        print(j, "////////////////////")
        for k in range (10):
            print(fibonacci(i, j, k))