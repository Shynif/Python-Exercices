def tri_selection(tab):
   for i in range(len(tab)-1):
      # Trouver le min
       min = i
       for j in range(i+1, len(tab)):
           if tab[min] > tab[j]:
               min = j
                
       tmp = tab[i]
       tab[i] = tab[min]
       tab[min] = tmp
       print(tab)
   return tab
# Programme principale pour tester le code ci-dessus
tab = [98, 22, 15, 32, 2, 74, 63, 70, 88,75, 76, 77]

print(tab)
print(tri_selection(tab))