from distance import *
def cout(villes):
    """donne le nombre total de km
    :return: total en km de la tournée
    """
    calcul = 0
    for i in range(0, len(villes)-1):
        calcul += distance(villes[i], villes[i+1])
    # ajout du retour au point de départ
    calcul += distance(villes[0], villes[-1])
    return calcul


