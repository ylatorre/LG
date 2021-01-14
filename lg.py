import random
from clear_screen import clear
import time
role_fix = ["Chasseur", "Cupidon", "Petite_Fille", "Sorciere", "Voyante"]
role_a_affecter = ["Amoureux"]  # A affecter en jeu

nbre_joueur = int(input("Entrez le Nombre de joueurs : "))
nbre_mechant = nbre_joueur*0.4
nbre_mechant = int(nbre_mechant)
print(nbre_mechant, nbre_joueur)
i = 0
listeJ = role_fix


def joueur():
    for i in range(nbre_mechant):
        listeJ.append('LG')
    if nbre_joueur > 9:
        vilagois = nbre_joueur - len(listeJ)
        print("nombre de {} vilagois ".format(vilagois))
        for i in range(vilagois):
            listeJ.append('vilagois')
    random.shuffle(listeJ)
    print(listeJ)
    print(len(listeJ))
    return listeJ


joueur()
clear()
i = 0
for i in range(nbre_joueur):
    print("ton role est : {}".format(listeJ[i]))
    wait = input("Press Enter to continue.")
    clear()
