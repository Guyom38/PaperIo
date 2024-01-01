def genere_matrice2D(dim_x, dim_y, valeur_defaut):
    return [[valeur_defaut for x in range(dim_y)] for i in range(dim_x)]

def autre_cote(valeur):
    return {0: 0, 1: 2, 2: 1}.get(valeur, valeur)