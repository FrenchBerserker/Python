import random

nb_min = random.randint(0, 1000)
nb_max = random.randint(nb_min + random.randint(0,10), 1111)

NOMBRE_MAGIQUE = random.randint(nb_min, nb_max)
NOMBRE_TENTATIVE = random.randint(1,10)

def programme():
    global NOMBRE_TENTATIVE

    print("Jouons au nombre magique !")
    print("Voici les règles:")
    print(f"Tu as {NOMBRE_TENTATIVE} tentatives pour trouver le bon chiffre, ou le bon nombre.")
    print(f"Il doit être compris entre {nb_min} et {nb_max} !")
    
    answer = 0
    while answer == 0 or answer != NOMBRE_MAGIQUE and NOMBRE_TENTATIVE != 0:
        answer = input("\nQuel est le nombre magique ? : ")
        try:
            answer = int(answer)
        except:
            answer = 0
        else:
            if answer <= nb_min or answer > nb_max:
                print(f"\nRappel : Le nombre magique est entre {nb_min} et {nb_max} !")
        if answer <= nb_min or answer >= nb_max:
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
        

