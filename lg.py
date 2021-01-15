import random
from clear_screen import clear
import time
role_fix = ["Chasseur", "Cupidon", "Petite_Fille", "Sorciere", "Voyante"]

nbre_joueur = int(input("Entrez le Nombre de joueurs : "))
nbre_mechant = nbre_joueur*0.4
nbre_mechant = int(nbre_mechant)
print(nbre_mechant, nbre_joueur)

i = 0
listeJ = ["Chasseur", "Cupidon", "Petite_Fille", "Sorciere", "Voyante"]


def joueur():
    for i in range(nbre_mechant):
        listeJ.append('LG{}'.format(i+1))
    if nbre_joueur > 9:
        villageois = nbre_joueur - len(listeJ)
        print("nombre de {} villageois ".format(villageois))
        for i in range(villageois):
            listeJ.append('villageois{}'.format(i+1))
    random.shuffle(listeJ)
    print(listeJ)
    print(len(listeJ))
    return listeJ


joueur()

wait = input("Press Enter to continue.")
clear()

i = 0
for i in range(nbre_joueur):
    print("ton role est : {} et ton numero est le {}".format(listeJ[i], i+1))
    wait = input("Press Enter to continue.")
    clear()


Equipe_LG = []
for i in range(nbre_mechant):
    Equipe_LG.append(listeJ.index("LG{}".format(i+1))+1)
Equipe_LG.sort()
print('Les LG sont :', Equipe_LG)


villageois = nbre_joueur - len(role_fix)-nbre_mechant
Equipe_Villagois = []
for i in range(villageois):
    Equipe_Villagois.append(listeJ.index("villageois{}".format(i+1))+1)
Equipe_Villagois.sort()
print('Les villagois sont :', Equipe_Villagois)

print(listeJ)
print("Debut de la 1er nuit, le village s'endors.")


print(listeJ.index("Cupidon")+1)


def couple():
    couple1 = int(input("Couple numero 1 : "))
    couple2 = int(input("Couple numero 2 : "))
    if couple1 == int(listeJ.index("Cupidon")+1) or couple2 == int(listeJ.index("Cupidon")+1) or couple1 == couple2:
        print("erreur ")
        couple()
    else:
        print("Les amoureux sont : {} et {}".format(
            listeJ[(couple1)-1], listeJ[(couple2)-1]))
        equipe_cupidon = [listeJ.index('Cupidon')+1, (couple1), (couple2)]
        equipe_cupidon.sort()
        print(equipe_cupidon)
        return couple1, couple2


couple()

print(listeJ)
print('Fin de la 1er nuit')
