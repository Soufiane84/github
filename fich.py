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


def inverse(mot):
    inv= mot[::-1]
    return inv

res = inverse("abc")
print(res)

