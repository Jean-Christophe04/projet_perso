
from calendar import c
import random

def alea_shifumi_avancer():
    shifumi = ["pierre", "papier", "ciseaux"]
    tempo = random.choice(shifumi)
    print(tempo)
    return tempo

def validation_coup_avancer(a):
    if( (a != "papier") and (a != "pierre") and (a != "ciseaux")):
        print("veuillez resaisir votre coup")
        return 2
    return 1

def verification_avancer(coup_a, coup_b):
    tempo = 0

    if(coup_a == coup_b):
        return tempo

    elif( (coup_a == "pierre") and (coup_b == "ciseaux")):
        tempo += 1
        return tempo

    elif( (coup_a == "pierre") and (coup_b == "papier")):
        tempo += 2
        return tempo

    elif( (coup_a == "papier") and (coup_b == "pierre")):
        tempo += 1
        return tempo

    elif( (coup_a == "papier") and (coup_b == "ciseaux")):
        tempo += 2
        return tempo

    elif( (coup_a== "ciseaux") and (coup_b == "pierre")):
        tempo += 2
        return tempo

    elif( (coup_a== "ciseaux") and (coup_b == "papier")):
        tempo += 1
        return tempo

def vainqueur_avancer(tour):
    i = 0
    compteur_1 = 0
    compteur_2 = 0

    while i < tour:

        joueur_1 = input()
        joueur_2 = alea_shifumi_avancer()

        while (validation_coup_avancer(joueur_1) != 1 ):
            print("les choix pouvant etre realise sont : papier  ciseaux  pierre")
            joueur_1 = input()
            
        if(verification_avancer(joueur_1, joueur_2) == 1):
            compteur_1 += 1
            print("victoire du joueur 1")
        elif(verification_avancer(joueur_1,joueur_2) == 2):
            compteur_2 += 1
            print("victoire du joueur 2")
        elif(verification_avancer(joueur_1,joueur_2) == 0):
            tour += 1
            print("egalite il faut rejoué")
        print("le joueur 1 a ", compteur_1," points et le joueur 2 a ", compteur_2 ,"point")
        i += 1

    if(compteur_1 < compteur_2):
        print("VICTOIRE DU JOUEUR 2 BRAVO")
    print ("VICTOIRE DU JOUEUR 1 BRAVO")
    
        
print("choisisez le noombre de manche")
a = input()
a = int(a)
print("la partie vas commencer attention a ne pas vous trompe dans l ecriture des mots")
print("vos different choix sont:  pierre  papier  et ciseaux")
vainqueur_avancer(a)       
        