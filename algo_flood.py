import pygame
import time

from constantes import *
from fonctions import *
import variables as VAR

class CJoueur:
    class CAlgo_Remplissage:
        
        
        def calcul_contour_zone(self):
            colorier(self.x, self.y, (128,128,128), 0.1)
            
            liste_de_points_de_depart = self.chercher_les_contours(self.x, self.y, False)
            
            print ("DEPART " + str(liste_de_points_de_depart))
            liste1 = []
            liste1.append( (self.x, self.y) )
            liste1.append( liste_de_points_de_depart[0] )
            
            liste2 = []
            liste2.append( (self.x, self.y) )
            liste2.append( liste_de_points_de_depart[1] )
            
            liste_contour_plus_rapide = self.chacun_son_tour(liste1, liste2)
            for x, y in liste_contour_plus_rapide:
                #colorier(x, y, (0,0,0), 0.01)
                self.CORPS.ajouter_morceau( x, y )
            
            #self.afficher(2)
            #colorier(0, 0, (200, 200, 200), 3)
            
            
        def chacun_son_tour(self, liste1, liste2):
            tour = 0
            
            while True:
                liste = liste1 if (tour % 2 == 0) else liste2
                x, y = liste[-1]                

                # prend le dernier element de la liste
                liste_points_suivants = self.chercher_les_contours(x, y, False)
                for xd, yd in liste_points_suivants:
                    if (xd, yd) not in liste:
                        liste.append( (xd, yd) )

                        # si le contour a atteint le serpent
                        if (xd, yd) in self.CORPS.elements:
                            return liste
                tour += 1
                    
            
        # trouver ou non les voisins
        def voisin(self, x, y, inverse):
            zones_recherche =  ( (0, 1), (-1, 0), (1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1) ) if inverse else ( (0, 1), (-1, 0), (1, 0), (0, -1) )
            
            liste_points = []            
            for xd, yd in zones_recherche:
                if inverse:
                    ajouter = (x + xd, y + yd) not in self.LISTE_ZONES
                else:
                    ajouter = (x + xd, y + yd) in self.LISTE_ZONES
                
                if ajouter:
                    liste_points.append( (x + xd, y + yd) )
                    
            return liste_points
        
        # trouver les deux points de depart
        def chercher_les_contours(self, x, y, depart):
            liste_points = []            

            # cherche voisin
            liste_voisins = self.voisin(x, y, False)
            for xd, yd in liste_voisins:
                #
                liste_voisins_bords = self.voisin(xd, yd, True)
                if len(liste_voisins_bords) > 0:
                    liste_points.append( (xd, yd) )                 
                        
            return liste_points
                    
                    
                    
            
            
            
            
            
            
            
            
               
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