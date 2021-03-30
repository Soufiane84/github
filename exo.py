somme = 100
continuer=False

while somme > 0 :
    choix = int(input("Choisissez un nombre entre 0 et 49 : "))

    mise = int(input("Entrez votre mise : "))
    if mise>somme:
        print("Vous n'avez pas assez d'argent (",somme,"euros).")
        continue
    somme -= mise
    gagnant = 40 #randrange(50)

    if choix == gagnant:
        mise = mise*3
        somme += mise
    elif (choix%2 == 0 and gagnant%2 == 0) or (choix%2 == 1 and gagnant%2 == 1):
        mise = mise*1.5
        somme +=mise
        
    print("\nVous avez maintenant ",somme, "euros.")
    
    quit = input("Continuer(C), quitter(Q)  : ")
    quit = quit.lower()
    if quit == "q":
        break
    