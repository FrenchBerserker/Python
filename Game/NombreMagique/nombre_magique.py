NOMBRE_MAGIQUE = 5
NOMBRE_TENTATIVE = 5


# Créer une fenêtre principale

def programme():
    global NOMBRE_TENTATIVE

    print("Jouons au nombre magie !")
    print("Voici les règles:")
    print("Tu as 5 tentatives pour trouver le bon chiffre, ou le bon nombre.")
    print("Il doit être compris entre 1 et 1000!")
    
    answer = 0
    while answer == 0 or answer != NOMBRE_MAGIQUE and NOMBRE_TENTATIVE != 0:
        answer = input("\nQuel est le nombre magique ? : ")
        try:
            answer = int(answer)
        except:
            answer = 0
        else:
            if answer <= 0 or answer > 999:
                print("\nRappel : Le nombre magique est entre 1 et 1000 !")
        if answer <= 0:
            print("Merci d'insérer un chiffre ou un nombre !")
        elif answer < NOMBRE_MAGIQUE:
            print("c'est plus !")
            NOMBRE_TENTATIVE -= 1 
            print(f"Il reste encore {NOMBRE_TENTATIVE} chance(s). Bonne chance !")
        elif answer > NOMBRE_MAGIQUE:
            print("c'est moins !")
            NOMBRE_TENTATIVE -= 1 
            print(f"Il reste encore {NOMBRE_TENTATIVE} chance(s). Bonne chance !")
        elif NOMBRE_TENTATIVE == 0:
            print("GAME OVER")
        elif answer == NOMBRE_MAGIQUE:
            print("C'est GAGNE !")

    if NOMBRE_TENTATIVE == 0:
        print("GAME OVER")


programme()
        

