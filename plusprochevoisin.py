from distance import *
from cout import *

listevisitee = []


def plusprochevoisin(villes):
    """
    Renvoie une tournée qui commence par Dijon puis ensuite tallant... [1, 4, 20, 45, 8, 47, 52, 35, 74, 71, 78, 42, 53,
    :param villes: liste de toutes les villes
    :return: /
    """
    listevilles = villes
    ville_depart = 0
    listevisitee.append(listevilles[ville_depart])
    del listevilles[ville_depart]
    ville_la_plus_proche = plus_proche(listevilles, listevisitee[-1])

    for i in range(0, len(listevilles) - 4):
        # on récupère l'index de la ville la plus proche dans la variable ville_la_plus_proche
        listevisitee.append(villes[ville_la_plus_proche])
        del listevilles[ville_la_plus_proche]
        ville_la_plus_proche = plus_proche(listevilles, listevisitee[-1])

    #rajout des villes manquantes
    listevisitee.append(listevilles[-1])
    del listevilles[-1]
    listevisitee.append(listevilles[1])
    del listevilles[1]
    listevisitee.append(listevilles[0])
    del listevilles[0]
    listevisitee.append(listevilles[0])
    del listevilles[0]

    # listevisitee.append(villes[ville_la_plus_proche])
    # del listevilles[ville_la_plus_proche]
    # print(listevilles)

    print("Plus proche voisin")
    print(str(listevisitee))
    print("Nombre de kilomètres : " + str(cout(listevisitee)))


def plus_proche(listevilles, villechoisie):
    """
    Effectue un tableau de tous les couts
    :param listevilles:
    :param villes: liste des villes pas encore visitées
    :param villechoisie:ville choisie dans le programme avec laquelle il faut faire le test de toutes les autres villes restantes dans le tableau
    :return: indexminimal : l'index de la ville la plus proche
    """
    listedistances = []
    # boucle pour toutes les villes
    for i in range(0, len(listevilles) - 1):
        # On teste si la villechoisie est dans la liste
        if villechoisie == listevilles[i]:
            listedistances.append(9999.99)
        else:
            listedistances.append(distance(villechoisie, listevilles[i]))
    return int(listedistances.index(min(listedistances)))
