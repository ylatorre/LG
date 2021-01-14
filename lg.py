import random
from clear_screen import clear
import time
role_fix= ["Chasseur","Cupidon","Petite_Fille","Sorciere","Voyante"]
role_a_affecter = ["Amoureux"] #A affecter en jeu

nbre_joueur = int(input("Entrez le Nombre de joueurs : "))
nbre_mechant = nbre_joueur*0.4
nbre_mechant = int(nbre_mechant)
print(nbre_mechant, nbre_joueur)
i = 0
listeJ = ["Chasseur","Cupidon","Petite_Fille","Sorciere","Voyante"]
def joueur():
    for i in range(nbre_mechant):
        listeJ.append('LG{}'.format(i+1))
    if nbre_joueur > 9:
        vilagois = nbre_joueur - len(listeJ)
        print("nombre de {} vilagois ".format(vilagois))
        for i in range(vilagois):
            listeJ.append('vilagois{}'.format(i+1))
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
print('Les LG sont :',Equipe_LG)

vilagois = nbre_joueur - len(role_fix)-nbre_mechant
Equipe_Villagois = []
for i in range(vilagois):
    Equipe_Villagois.append(listeJ.index("vilagois{}".format(i+1))+1)
Equipe_Villagois.sort()
print('Les villagois sont :',Equipe_Villagois)


print("Debut de la 1er nuit, le village s'endors.")

amoureux = input("Cupidon designe 2 joueurs :").split()
Equipe_Cupidon = amoureux.append(listeJ.index('Cupidon')+1)
print("Les amoureux sont :",amoureux)
print('Fin de la 1er nuit')
print('Debut de la 1er journee')