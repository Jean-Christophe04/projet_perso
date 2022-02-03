import random


def alea_shifumi():
    shifumi = ["pierre", "papier", "ciseaux"]
    tempo = random.choice(shifumi)
    print(tempo)
    return tempo

def verification(x, y):

    tempo = 0

    if(x == y):
        return tempo

    elif( (x == "pierre") and (y == "ciseaux")):
        tempo += 1
        return tempo

    elif( (x == "pierre") and (y == "papier")):
        tempo += 2
        return tempo

    elif( (x == "papier") and (y == "pierre")):
        tempo += 1
        return tempo

    elif( (x == "papier") and (y == "ciseaux")):
        tempo += 2
        return tempo

    elif( (x == "ciseaux") and (y == "pierre")):
        tempo += 2
        return tempo

    elif( (x == "ciseaux") and (y == "papier")):
        tempo += 1
        return tempo
    

def vainqueur(a,b,tour):
    i = 0
    while i < tour:

        joueur_1 = alea_shifumi()
        joueur_2 = alea_shifumi()

        if(verification(joueur_1, joueur_2) == 1):
            a += 1
        elif(verification(joueur_1, joueur_2) == 2):
            b += 1
        print("le joueur 1 a ",a,"points et le joueur 2 a ",b," points")
        if(verification(joueur_1,joueur_2) == 0):
            tour += 1
        i += 1



compteur_1 = 0
compteur_2 = 0

vainqueur(compteur_1, compteur_2, 5)





