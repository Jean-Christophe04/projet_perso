def mot_choisi():
    print("choisisez le mot a faire devinez : ")
    mot = input()
    return mot

def demande_lettre():
    print("proposez une lettre pour le mot \n")
    lettre = input()
    return lettre 

def lettre_dans_un_mot(mot, lettre_proposez, tab):
    if lettre_proposez in mot:
        print("lettre trouver")
        for i, car in enumerate(mot):
            if car == lettre_proposez:
                tab[i] = lettre_proposez
                print(tab[i])
    
    return tab


def nombre_restant(taille,tab):
    k = 0
    compteur = taille
    while k < taille:
        if tab[k] != "_":
            compteur = compteur - 1
        if compteur == 0:
            return 2
        k += 1

            

def verif_tableau(tableau,valeur):
    tableau.append(valeur)
    print(tableau)
    return tableau

def dessine_pendu(cpt):
    if cpt == 9:
        print("_______")
    elif cpt == 8:
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("_______")
    elif cpt == 7:
        print("    ______")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("_______")
    elif cpt == 6:
        print("    ______")
        print("   |      |")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("_______")
    elif cpt == 5:
        print("    ______")
        print("   |      |")
        print("   |      O")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("_______")
    elif cpt == 4:
        print("    ______")
        print("   |      |")
        print("   |      O")
        print("   |      |")
        print("   |")
        print("   |")
        print("   |")
        print("_______")
    elif cpt == 3:
        print("    ______")
        print("   |      |")
        print("   |      O")
        print("   |      |/")
        print("   |")
        print("   |")
        print("   |")
        print("_______")
    elif cpt == 2:
        print("    ______")
        print("   |      |")
        print("   |      O")
        print("   |     \|/")
        print("   |")
        print("   |")
        print("   |")
        print("_______")
    elif cpt == 1:
        print("    ______")
        print("   |      |")
        print("   |      O")
        print("   |     \|/")
        print("   |     /")
        print("   |")
        print("   |")
        print("_______")
    elif cpt == 0:
        print("    ______")
        print("   |      |")
        print("   |      O")
        print("   |     \|/")
        print("   |     / \*")
        print("   |")
        print("   |")
        print("_______")


def evaluation_mot():
    valeur = mot_choisi()
    taile_valeur = len(valeur)
    compteur_vie = 10
    tab = ["_" for _ in range(taile_valeur)]
    tab_erreur = []
    i = 0

    for i in range(10):
        print("\n")
    
    while i < taile_valeur:
        print(" "+tab[i], end=" ")
        i += 1
    print("\n")

    while True:    
        j = 0
        lettre_proposez = demande_lettre()
        if lettre_proposez not in valeur:
            print("erreur mauvaise lettre")
            if lettre_proposez not in tab_erreur:
                verif_tableau(tab_erreur,lettre_proposez)
            compteur_vie -= 1
            print(compteur_vie)
            dessine_pendu(compteur_vie)
        elif lettre_proposez in valeur :
            lettre_dans_un_mot(valeur, lettre_proposez, tab)
            while j < taile_valeur:
                print(" "+tab[j], end= "")
                j += 1
            print("\n")
        if compteur_vie == 0:
            print("vous avez perdu le mot que vous cherchez etait "+valeur+"\n")
            break
        if nombre_restant(taile_valeur,tab) == 2:
            print("vous avez trouvé toutes les lettres bravo \n")
            print(valeur)
            break 


evaluation_mot()