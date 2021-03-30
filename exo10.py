def convert_temp():
    entree = input("Entrer la température : ")

    fahren=False
    celcius=False

    unite = entree[-1]
    unite = unite.lower()

    valeur = entree[:-1]
    valeur=int(valeur)

    if unite == 'c':
        res = valeur * (9/5) + 32
        celcius = True
    elif unite == 'f':
        res = (5/9)*(valeur-32)
        fahren = True
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
        continue