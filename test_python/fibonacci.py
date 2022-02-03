import random

nombre_affiche = int(input("Entre le nombre de chiffre de la suite de fibonacci que vous voulez afficher"))

def suite_fibo():
    a = 0
    b = 1
    total = 0
    for i in range(nombre_affiche):
        print(total)
        a = b
        b = total
        total = a + b

suite_fibo()