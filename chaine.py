# -*- coding : UTF-8 -*-

"""
liste1 = ["lapin", "chat", "chien", "chiot", "dragon", "ornithorynque"]

for elem in liste1:
    print(elem)

liste1.reverse()


liste1.sort()


liste1.append("troll")


animaux = ["lapin", "chat", "chien", "chiot"]
for i in animaux:
    liste1.remove(i)
print(liste1)

"""





import random


#SANS BOOLEAN
"""
tableau_jeu=[]
for i in range (0,10) :
    tableau_jeu.append(random.randint (1,10))
print(tableau_jeu)

nb = int(input("Entrez le chiffre : "))
for i in range(0,len(tableau_jeu)):
    if nb == tableau_jeu[i]:
        print("Gagné")
        break
    if i == len(tableau_jeu)-1:
        print("Perdu")
"""

"""
tableau_jeu=[]
for i in range (0,10) :
    tableau_jeu.append(random.randint (1,10))
tableau_jeu.sort()
print(tableau_jeu)

nb = int(input("Entrez le chiffre : "))
for i in range(0,len(tableau_jeu)):
    if nb == tableau_jeu[i]:
        print("Gagné")
        break
    if i == len(tableau_jeu)-1 or tableau_jeu[i]>nb:
        print("Perdu")
        break

 """




#AVEC BOOLEAN
""" 
tableau_jeu=[]
for i in range (0,10) :
    tableau_jeu.append(random.randint (1,10))
print(tableau_jeu)

trouve=False
nb = int(input("Entrez le chiffre : "))
for item in tableau_jeu:
    if nb == item:
        trouve = True
        print("Gagné")
        break
if trouve == False:
    print("Perdu")
 """

""" 
tableau_jeu=[]
for i in range (0,10) :
    tableau_jeu.append(random.randint (1,10))
tableau_jeu.sort()
print(tableau_jeu)

trouve=False
nb = int(input("Entrez le chiffre : "))
for item in tableau_jeu:
    if nb == item:
        trouve = True
        print("Gagné")
        break
    if item>nb:
        break
if trouve == False:
    print("Perdu")
 """