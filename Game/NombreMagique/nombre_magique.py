NOMBRE_MAGIQUE = 5
NOMBRE_TENTATIVE = 5


# Créer une fenêtre principale

def programme():
    global NOMBRE_TENTATIVE

    print("Jouons au nombre magie !")
    print('''
Voici les règles:
Tu as 5 tentatives pour trouver le bon chiffre, ou le bon nombre.
Il doit être compris entre 0 et 100!''')
    
    answer = -1
    while answer != NOMBRE_MAGIQUE and NOMBRE_TENTATIVE != 0:
        answer = int(input("\nQuel est le nombre magique ? : "))
        if answer < NOMBRE_MAGIQUE:
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
        

