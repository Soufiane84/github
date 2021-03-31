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
    print(texte)

replace = {"1": "i", "3": "e"} 
texte =  "La v13 3st un myst3r3 qu'1l faut v1vr3, et non un probl3m3 a r3soudr3. Gandh1"

res = replace_multiple(texte, replace)
print(res)
"""