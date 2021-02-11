# Clappin emoji message

msg = input("message : ")
arr = msg.split(" ")
out = ""

for i in arr :
    out += i
    out += " :clap: "
print(out)