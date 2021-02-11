import random as r

L = int(input("Longueur ? "))
l = int(input("Largeur ? "))

def fonction_ten_print(L, l) :
    ten_print = "" # On pourrait faire aussi avec une liste mais ça c'est un challenge pour vous ;)
    for i in range(l) :
        for j in range(L) :
            '''# Méthode n°1 :
            if (r.random() < 0.5) :
                ten_print += "/"
            else :
                ten_print += "\\"
            '''
            # Méthode n°2 :
            ten_print += r.choice(["/", "\\", "O", "#"])
        ten_print += '\n'
    print(ten_print)

fonction_ten_print(L, l)