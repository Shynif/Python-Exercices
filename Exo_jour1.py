
partie_finit = "Y"
baton = 20
tour = True # True -> Joueur 1      False -> Joueur 2

while partie_finit == "Y" :
    
    baton_dessin = ""
    for i in range (baton):
        baton_dessin += "|"
    print(baton_dessin)

    if (tour == True) :
        entre = int(input("Joueur 1, combien de bâtons voulez vous prendre ?   1/2/3 \n"))
    else :
        entre = int(input("Joueur 2, combien de bâtons voulez vous prendre ?   1/2/3 \n"))

    if entre > 3 :
        entre = 3
    if entre <= 0 :
        entre = 1
    
    baton -= entre

    if (baton <= 0) :

        if (tour == True) :
            print("Joueur 1 a gagné !")
        else :
            print("joueur 2 a gagné !")
        
        partie_finit = input("Voulez vous continuer la partie ?     Y/N \n")
        
        baton = 20
        tour = False
    
    tour = not tour