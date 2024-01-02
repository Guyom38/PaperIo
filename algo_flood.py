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

            # retourne les directions a explorer autour de la case, du coté interieur !!!     
            def trouve_faces(x, y):
                if self.CORPS.id_interieur == 0:
                    print( str( (self.CORPS.LIMITE.x, self.CORPS.LIMITE.y, self.CORPS.elements[(self.CORPS.LIMITE.x, self.CORPS.LIMITE.y)])) )
                    raise ExceptionType("L'interieur n'a pas été déterminé.")
                
                faces = []
                for direction, id in self.CORPS.elements[ (x, y) ].face.items():
                    if id == self.CORPS.id_interieur:
                        faces.append(direction)
                return faces    
            
                
            def ajouter_zone(x, y):
                if self.MOTEUR.TERRAIN.est_ce_sur_terrain(x, y):
                    if (x, y) not in self.LISTE_ZONES: 
                        if (x, y) not in zones_explorees and (x, y) not in liste_zones_a_explorer:
                            if (x, y) not in self.CORPS.elements:
                                liste_zones_a_explorer.add((x, y))
                                
      
                    

            # Initialisation des zones à explorer   
            #print( str(self.CORPS.elements.keys()))         
            for coord, _ in self.CORPS.elements.items():
                x, y = coord
                for face in trouve_faces(x, y):
                    xd, yd = FACES[face]  
                    #colorier(x + xd, y + yd, (64,64,64), 0.01)  
                    ajouter_zone(x + xd, y + yd)

            # Propagation
            #print( str(liste_zones_a_explorer))
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
                    #colorier(x, y, (0,128,0), 0.01)   