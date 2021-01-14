

def couple():
    couple1 = int(input("Couple numero 1 : "))
    couple2 = int(input("Couple numero 2 : "))
    if couple1 != 6 and couple2 != 6:
        print("erreur")
        couple()
    else:
        print("Yes")
couple()s