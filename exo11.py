# QR Code generator

from random import randint

f = open("test.pbm", "w")

width = 50
height = 50

result = "P1\n"+str(width)+" "+str(height)+"\n"

for x in range(width) :
    for y in range(height) :
        if (randint(0,1) == 0) :
            result += "0 "
        else :
            result += "1 "
    result += "\n"

f.write(result)
f.close()