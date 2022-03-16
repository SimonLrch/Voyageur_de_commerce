import math


def distance(ville1, ville2):
    """
    Fonction qui renvoie la distance entre deux villes avec la formule de haversine
    :param ville1:première ville
    :param ville2:deuxième ville
    :return:calucl renvoyé par la formule de haversine
    """
    r = 6371
    x1 = ville1.longitude
    x2 = ville2.longitude
    y1 = ville1.latitude
    y2 = ville2.latitude
    calcul = math.fabs(r * math.acos((math.sin(math.radians(y1)) * math.sin(math.radians(y2))) + (math.cos(math.radians(y1)) * math.cos(math.radians(y2)) * math.cos(math.radians(x1) - math.radians(x2)))))

    return calcul
