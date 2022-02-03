def test_fonction():
    a = input()
    b = input()
    a = int(a)
    b = int(b)
    for i in range(10):
        c = a * b
        a = a + (i*2)
        b = b +((1/2) * i)
        print(c)

# test_fonction()

def tes_fonction2():
    a = 1
    for i in range(6):
        b = a * i
        print(b, end=" ")
    print("\n")

# tes_fonction2()

def caractere_mot():
    mot = "evaluation"
    cherche = input()
    for i, car in enumerate(mot):
        if car == cherche:
            print(i)

# caractere_mot()

def lettre_pas_mot():
    mot = "evaluation"
    recherche = input()
    if recherche not in mot :
        print("ta mere la pute")
    else :
        print("good JOB")

lettre_pas_mot()