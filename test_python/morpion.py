from re import T


plateau = [" " for _ in range(9)]


def affiche_tableau(p, gagnant = None):
    print(" " + p[0] + " | " + p[1] + " | " + p[2] + " ")
    print("---+---+---")
    print(" " + p[3] + " | " + p[4] + " | " + p[5] + " ")
    print("---+---+---")
    print(" " + p[6] + " | " + p[7] + " | " + p[8] + " ")
    print("---+---+---")
    if(gagnant):
        print("""* Partie terminé : le joueur {0} a gagné.*""".format(gagnant))

def morpion():
    joueur = "X"
    tour = 0

    while True:
        affiche_tableau(plateau)
        print("> tour du joueur" + joueur + ".Entré un nombre entre 1 et 9")
        move = int(input()) - 1

        if plateau[move] == " ":
            plateau[move] = joueur
            tour += 1
        else :
            print(" cette case est deja prise choisissez en une autre ")
            continue
        if plateau[0] == plateau[1] == plateau[2] !=  " "\
        or plateau[0] == plateau[4] == plateau[8] !=  " "\
        or plateau[0] == plateau[3] == plateau[6] !=  " "\
        or plateau[1] == plateau[4] == plateau[7] !=  " "\
        or plateau[2] == plateau[5] == plateau[8] !=  " "\
        or plateau[3] == plateau[4] == plateau[5] !=  " "\
        or plateau[6] == plateau[7] == plateau[8] !=  " "\
        or plateau[2] == plateau[4] == plateau[6] !=  " ":
            affiche_tableau(plateau, joueur)
            break
        if tour == 9:
            affiche_tableau(plateau)
            print(" egalite ")
            break   
        joueur = "O" if joueur == "X" else "X"

morpion()