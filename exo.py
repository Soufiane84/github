somme = 100

while somme > 0 :
    gagnant = 40 #randrange(50)

    choix = int(input("\nChoisissez un nombre entre 0 et 49 : "))
    while choix<0 or choix>49:
        print("Restez dans l'intervalle [0-49].")
        choix = int(input("\nChoisissez un nombre entre 0 et 49 : "))


    mise = int(input("Entrez votre mise : "))
    while mise>somme:
        print("Vous n'avez pas assez d'argent (",somme,"euros).")
        mise = int(input("Entrez votre mise : "))

    somme -= mise

    if choix == gagnant:
        mise = mise*3
        somme += mise
    elif (choix%2 == gagnant%2) :
        mise = mise*1.5
        somme +=mise

    if somme > 0:
        print("\nVous avez maintenant ",somme, "euros.")
    else:
        print("Perdu, vous n'avez plus d'argent.")
        break

    quit = input("Continuer(C), quitter(Q)  : ")
    quit = quit.lower()
    if quit == "q":
        break
