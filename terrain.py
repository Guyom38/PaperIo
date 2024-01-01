import pygame
from fonctions import *
import variables as VAR

class CTerrain:
    def __init__(self, moteur):
        self.MOTEUR = moteur
        
        self.dimension_x, self.dimension_y = VAR.resolution_x // VAR.cellule, VAR.resolution_y // VAR.cellule
                    
    
    def est_ce_sur_terrain(self, x, y):
        return ( 0 <= x < self.dimension_x and 0 <= y < self.dimension_y)  
    
    def afficher(self):
        # --- affiche la grille
        for y in range(self.dimension_y):
            for x in range(self.dimension_x):
                xc = x * VAR.cellule
                yc = y * VAR.cellule
                
                pygame.draw.rect(VAR.fenetre, (32, 32, 32), (xc, yc, VAR.cellule, VAR.cellule), 1)
        
        # --- affiche les zones du joueurs
        for x, y in self.MOTEUR.JOUEUR.LISTE_ZONES:
            xc = x * VAR.cellule
            yc = y * VAR.cellule
            
            pygame.draw.rect(VAR.fenetre, (255, 0, 0), (xc, yc, VAR.cellule, VAR.cellule), 0)      
            
                