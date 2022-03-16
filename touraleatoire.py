from random import *
from cout import *
def touraleatoire(villes):
    """fait un tour aléatoirement
    :return: liste des villes en aléatoire
    """
    shuffle(villes)
    print(str(villes))
    print("Nombre de kilomètres : " + str(cout(villes)))
