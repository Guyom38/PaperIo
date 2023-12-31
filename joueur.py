import pygame
from fonctions import *
import variables as VAR

from corps import *
class CJoueur:
    def __init__(self, moteur):
        self.MOTEUR = moteur
        
        self.x, self.y = 0, 0        
        self.couleur = (255, 255, 0)
        self.ecriture = pygame.font.SysFont('arial', 10) 
        
        self.CORPS = CCorps()
        
    def afficher(self):
        for index, element in enumerate(self.CORPS.elements):
            x, y = element.x, element.y
            xc, yc = x * VAR.cellule, y * VAR.cellule
            pygame.draw.rect(VAR.fenetre, (255, 255, 0), (xc, yc, VAR.cellule, VAR.cellule), 0)    
            
            image_texte = self.ecriture.render(str(len(self.CORPS.elements) - index), True, (0,0,0)) 
            #VAR.fenetre.blit(image_texte, (xc + ((VAR.cellule - image_texte.get_width()) // 2), yc + ((VAR.cellule - image_texte.get_height()) // 2)))
            
            d = 4
            if element.face[ENUM_DIR.DROITE] == 1:
                pygame.draw.rect(VAR.fenetre, (0, 0, 255), (xc+ VAR.cellule-d, yc, d, VAR.cellule), 0)   
            if element.face[ENUM_DIR.GAUCHE] == 1:
                pygame.draw.rect(VAR.fenetre, (0, 0, 255), (xc, yc, d, VAR.cellule), 0)   
            if element.face[ENUM_DIR.HAUT] == 1:
                pygame.draw.rect(VAR.fenetre, (0, 0, 255), (xc, yc, VAR.cellule, d), 0)   
            if element.face[ENUM_DIR.BAS] == 1:
                pygame.draw.rect(VAR.fenetre, (0, 0, 255), (xc, yc+VAR.cellule-d, VAR.cellule, d), 0)   
            
            if element.face[ENUM_DIR.DROITE] == 2:
                pygame.draw.rect(VAR.fenetre, (0, 128, 128), (xc+ VAR.cellule-d, yc, d, VAR.cellule), 0)   
            if element.face[ENUM_DIR.GAUCHE] == 2:
                pygame.draw.rect(VAR.fenetre, (0, 128, 128), (xc, yc, d, VAR.cellule), 0)   
            if element.face[ENUM_DIR.HAUT] == 2:
                pygame.draw.rect(VAR.fenetre, (0, 128, 128), (xc, yc, VAR.cellule, d), 0)   
            if element.face[ENUM_DIR.BAS] == 2:
                pygame.draw.rect(VAR.fenetre, (0, 128, 128), (xc, yc+VAR.cellule-d, VAR.cellule, d), 0)   
                
            image_texte = self.ecriture.render(str(element.direction), True, (0,0,0)) 
            VAR.fenetre.blit(image_texte, (xc + ((VAR.cellule - image_texte.get_width()) // 2), yc + ((VAR.cellule - image_texte.get_height()) // 2)))
           
        
        #xc, yc = self.x * VAR.cellule, self.y * VAR.cellule    
        #pygame.draw.rect(VAR.fenetre, (255, 255, 0), (xc, yc, VAR.cellule, VAR.cellule), 0)    
        #pygame.draw.rect(VAR.fenetre, (128, 128, 0), (xc, yc, VAR.cellule, VAR.cellule), 2)    
        
        
        
        