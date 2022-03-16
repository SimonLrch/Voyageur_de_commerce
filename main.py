villes = []
from affichetour import *
from cout import *
from distance import *
from plusprochevoisin import *
from touraleatoire import *


class Ville:
    def __init__(self, numeroville, nomville, latitude, longitude):
        """
        :param numeroville: numéro de la ville
        :param nomville: nom de la ville
        :param latitude: latitude de la ville
        :param longitude: longitude de la ville
        """

        self.longitude = float(longitude)
        self.latitude = float(latitude)
        self.nomville = nomville
        self.numeroville = numeroville

    def __repr__(self):
        """ Renvoie une chaine de caractère quand on appelle la classe
        :return: str
        """
        return f"{self.numeroville}"


# Main
# open the file in read mode
if __name__ == "__main__":
    with open('top80.txt', "r", encoding='utf-8') as file:
        lines = file.read().splitlines()
        for line in lines:
            x = line.split()
            v = Ville(x[0], x[1], x[2], x[3])
            villes.append(v)

    plusprochevoisin(villes)
