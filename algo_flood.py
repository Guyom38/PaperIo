import pygame
import time

from constantes import *
from fonctions import *
import variables as VAR

class CJoueur:
    class CAlgo_Remplissage:
        def capture_zone(self):
            t = time.time()
            
            liste_zones_a_explorer = set()
            zones_explorees = set()

                 
                
            def ajouter_zone(x, y):
                if self.MOTEUR.TERRAIN.est_ce_sur_terrain(x, y):
                    if (x, y) not in self.LISTE_ZONES:
                        if (x, y) not in zones_explorees and (x, y) not in liste_zones_a_explorer:
                            if (x, y) not in self.CORPS.elements :
                                liste_zones_a_explorer.add((x, y))
                                
                                colorier(x, y, (128,0,0))   
                    

            # Initialisation des zones à explorer            
            for coord, element in self.CORPS.elements.items():
                x, y = coord
                for face in self.CORPS.trouve_faces(x, y):
                    xd, yd = FACES[face]               
                    ajouter_zone(x + xd, y + yd)

            # Propagation
            while liste_zones_a_explorer:
                x, y = liste_zones_a_explorer.pop()
                zones_explorees.add((x, y))

                for dx, dy in [(0, 1), (-1, 0), (1, 0), (0, -1)]:
                    ajouter_zone(x + dx, y + dy)

            for x, y in self.CORPS.elements:
                zones_explorees.add((x, y))
            
            print( round(time.time() - t, 3) )   
            
            # Affichage des zones capturées
            for x, y in zones_explorees:
                if (x, y) not in self.LISTE_ZONES:
                    self.LISTE_ZONES.append( (x, y) )   
                    colorier(x, y, (0,128,0))   