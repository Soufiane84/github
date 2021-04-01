""" 
def searchC(mot, chaine):
    if mot in chaine:
        indice = chaine.find(mot)
        return indice
    else:
        return False

position = searchC("test", "fhdfjdtefjdjf")
print(position)
"""


""" 
def replace_multiple(texte, replace):
    for i, j in replace.items():
        texte = texte.replace(i, j)
    return texte

replace = {"1": "i", "3": "e"} 
texte =  "La v13 3st un myst3r3 qu'1l faut v1vr3, et non un probl3m3 a r3soudr3. Gandh1"

res = replace_multiple(texte, replace)
print(res)
"""


""" 
def compteur(lettre, chaine):
    cpt=0
    for letter in chaine:
        if letter == lettre:
            cpt+=1
    return cpt

res= compteur('a', "hgfhgf")
print(res)
"""



""" 
def inverse(mot):
    inv= mot[::-1]
    return inv

res = inverse("abc")
print(res)
"""


""" 
import os
os.chdir("C:/Users/Soufiane/Desktop/AJC/Python/github")

def Nbrligne(name_fic):
    with open(name_fic, 'r') as mon_fic:
        count=0
        for line in mon_fic:
            if line !="\n":
                count+=1
        return count

res= Nbrligne("Demi.txt")
print(res)
"""

""" 
import os
os.chdir("C:/Users/Soufiane/Desktop/AJC/Python/github")


with open("Demi.txt", 'r') as mon_fic:
    txt = mon_fic.read()
mon_fic.close()


with open("La_mesure_de_lhomme.txt", 'a') as mon_fic2:
    mon_fic2.write(txt)

with open("La_mesure_de_lhomme.txt", 'r') as mon_fic2:
    res = mon_fic2.read()


print(res)

mon_fic2.close()
 """


""" 
import pickle
with open ('binary.txt', 'rb') as le_bin :
    mon_depickler = pickle.Unpickler(le_bin)
    liste = mon_depickler.load()

print(liste) """