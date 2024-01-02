import pygame, random
from fonctions import *
import variables as VAR

class CTerrain:
    def __init__(self, moteur):
        self.MOTEUR = moteur
        self.bitmap = None
        self.dimension_x, self.dimension_y = VAR.resolution_x // VAR.cellule, VAR.resolution_y // VAR.cellule

    def est_ce_sur_terrain(self, x, y):
        return ( 0 <= x < self.dimension_x and 0 <= y < self.dimension_y)  
    
    
    def afficher(self):
        if self.bitmap == None:
            self.bitmap = pygame.Surface( (VAR.resolution_x, VAR.resolution_y), pygame.SRCALPHA)
            for i in range(10):
                x1 = random.randint(0, self.dimension_x - 4) 
                y1 = random.randint(0, self.dimension_y - 4) 
                x2 = random.randint(1, self.dimension_x - x1) 
                y2 = random.randint(1, self.dimension_y - y1) 
                pygame.draw.rect(self.bitmap, (223, 250, 239, random.randint(0, 255)),  (x1 * VAR.cellule, y1 * VAR.cellule, x2 * VAR.cellule, y2 * VAR.cellule), 0 )
        
        VAR.fenetre.fill((251,251,237))
        VAR.fenetre.blit(self.bitmap, (0, 0))   
        
        if 1 == 2:           
            # --- affiche la grille
            for y in range(self.dimension_y):
                for x in range(self.dimension_x):
                    xc = x * VAR.cellule
                    yc = y * VAR.cellule
                    
                    pygame.draw.rect(VAR.fenetre, (200, 200, 200), (xc, yc, VAR.cellule+1, VAR.cellule+1), 1)
        
        # --- affiche les zones du joueurs
        image_tmp = self.MOTEUR.JOUEUR.images['tete']  
        liste_triee = sorted(self.MOTEUR.JOUEUR.LISTE_ZONES, key=lambda coord: coord[1])
        
        for x, y in liste_triee:
            xc = x * VAR.cellule
            yc = y * VAR.cellule
            
            #pygame.draw.rect(image_tmp, self.couleur_tete, (0, 0, VAR.cellule, VAR.cellule), 0)
            #pygame.draw.rect(image_tmp, self.couleur, (0, VAR.cellule, VAR.cellule, VAR.taille_tete), 0)
            #pygame.draw.rect(VAR.fenetre, (255, 0, 0), (xc, yc, VAR.cellule, VAR.cellule), 0)      
            VAR.fenetre.blit(image_tmp, (xc, yc - VAR.taille_tete))          