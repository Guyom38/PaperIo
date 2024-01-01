import pygame
from fonctions import *
import variables as VAR

class CTerrain:
    def __init__(self, moteur):
        self.MOTEUR = moteur
        
        self.dimension_x, self.dimension_y = VAR.resolution_x // VAR.cellule, VAR.resolution_y // VAR.cellule
        self.initialiser()
    
    
    def initialiser(self):
        self.zone = genere_matrice2D(self.dimension_x, self.dimension_y, 0)
        
        
        

                    
        
    def afficher(self):
        for y in range(self.dimension_y):
            for x in range(self.dimension_x):
                xc = x * VAR.cellule
                yc = y * VAR.cellule
                
                if not self.zone[x][y] == 0:
                    pygame.draw.rect(VAR.fenetre, (255, 0, 0), (xc, yc, VAR.cellule, VAR.cellule), 0)                    
                pygame.draw.rect(VAR.fenetre, (32, 32, 32), (xc, yc, VAR.cellule, VAR.cellule), 1)
                
        for x, y in self.MOTEUR.JOUEUR.LISTE_ZONES:
            xc = x * VAR.cellule
            yc = y * VAR.cellule
            
            pygame.draw.rect(VAR.fenetre, (255, 0, 0), (xc, yc, VAR.cellule, VAR.cellule), 0)      
            
                