""" 
def convert_temp():
    entree = input("\nEntrer la température : ")

    fahren=False
    celcius=False

    unite = entree[-1]
    unite = unite.lower()

    valeur = entree[:-1]
    valeur=float(valeur)

    if unite == 'c':
        res = valeur * (9/5) + 32
        celcius = True
    elif unite == 'f':
        res = (5/9)*(valeur-32)
        fahren = True
    else:
        res = 0
    return res, fahren, celcius 



while 1:
    res, fahren, celcius = convert_temp()
    if fahren:
        print(round(res),"C")
        break
    elif celcius:
        print(round(res), "F")
        break 
    else:
        print("Veuillez entrer une unité valide !")
        continue
"""


""" 
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

def combiner(*args):
    dic={}
    for elem in args:
        dic.update(elem)
    return dic


res = combiner(dic1,dic2)
print(res)
# dic = {**dic1,**dic2,**dic3}
"""


""" 
import datetime
today = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
print(today)
"""


""" 
import datetime
today = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
print(today)
"""


""" 
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0],color_list[-1])
"""


""" 
import os
print(os.name)

import platform
print(platform.system())
print(platform.release())
 """


""" 
import pickle

liste = ["test1","test2","test3",1,2,3]

with open("binary.txt", 'wb') as list_bin:
    mon_pickler = pickle.Pickler(list_bin)
    mon_pickler.dump(liste)
"""