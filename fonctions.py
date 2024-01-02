
import math
import pygame, time

import variables as VAR


def genere_matrice2D(dim_x, dim_y, valeur_defaut):
    return [[valeur_defaut for x in range(dim_y)] for i in range(dim_x)]

def autre_cote(valeur):
    return {0: 0, 1: 2, 2: 1}.get(valeur, valeur)



def calculer_distance(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def colorier(x, y, c, d = 0.001):                 
    xc = (x * VAR.cellule) + (VAR.cellule //2)
    yc = (y * VAR.cellule) + (VAR.cellule //2)
                            
    pygame.draw.circle(VAR.fenetre, c, (xc, yc), VAR.cellule //2, 0)
    pygame.display.update()
    time.sleep(d) 
    
class ExceptionType(Exception):
    def __init__(self, message):
        super().__init__(message)

