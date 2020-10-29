import random

# On génère au hasard 10 notes entre 0 et 20
liste_notes = [random.randint(0, 20) for _ in range(10)]


def get_minimum(l):
    """Trouve le minimum d'une liste de nombres"""
    minimum = None
    for nombre in l:
        # A la première valeur regardée est forcément
        # est forcémentla plus petit qu'on a déjà regardé

        if minimum is None:
            minimum = nombre

        elif nombre < minimum:
            minimum = nombre

        else:
            pass
    return minimum


def get_somme(l):
    """Calcule la somme d'une liste de nombres"""
    somme = 0
    for nombre in l:
        somme += nombre


# On vérifie que notre fonction renvoie le même résultat que
assert get_minimum(liste_notes) == min(liste_notes)
