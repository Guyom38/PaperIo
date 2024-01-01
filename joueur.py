import pygame, time, random

from fonctions import *
import variables as VAR

from corps import *
from algo_flood import *


class CJoueur(CJoueur.CAlgo_Remplissage):
    def __init__(self, moteur):
        self.MOTEUR = moteur
        
        self.x, self.y = 10, 10   
        self.direction = ENUM_DIR.AUCUN
             
        self.couleur = (255, 255, 0)
        self.ecriture = pygame.font.SysFont('arial', 10) 
        self.vitesse = 0.1
        self.vitesse_timer = time.time()
        
        self.CORPS = CCorps(moteur)
        self.LISTE_ZONES = []
        
        
    def creer_la_zone_de_depart(self):
        self.x = random.randint(4, self.MOTEUR.TERRAIN.dimension_x -4)
        self.y = random.randint(4, self.MOTEUR.TERRAIN.dimension_y -4)
        
        for y in range(-2, 2):
            for x in range(-2, 2):
                if self.MOTEUR.TERRAIN.est_ce_sur_terrain(self.x + x, self.y + y):
                    self.LISTE_ZONES.append( (self.x + x, self.y + y) )
                    
        if self.x > self.MOTEUR.TERRAIN.dimension_x // 2:
            self.direction = ENUM_DIR.GAUCHE
            self.x -= 2
        else:
            self.direction = ENUM_DIR.DROITE
            self.x += 1           
                    
        self.CORPS.regime()
                
                    
    

            
                
    def se_deplacer(self):
        if time.time() - self.vitesse_timer < self.vitesse:
            return
        
        self.vitesse_timer = time.time()
        xd, yd = FACES[self.direction]
        self.x += xd
        self.y += yd
        
        if not (self.x, self.y) in self.LISTE_ZONES:
            self.CORPS.ajouter_morceau( self.x, self.y )
            
        else:        
            if len(self.CORPS.elements) > 4:
                self.capture_zone()
                self.CORPS.regime()
        
    def afficher_faces(self, element, x, y):
                xc, yc = x * VAR.cellule, y * VAR.cellule
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
                     
    def afficher(self):
        if len(self.CORPS.elements) > 0:
          
            for index, donnees in enumerate(self.CORPS.elements.items()):
                coord, element = donnees            
                x, y = coord
                
                xc, yc = x * VAR.cellule, y * VAR.cellule
                pygame.draw.rect(VAR.fenetre, (255, 255, 0), (xc, yc, VAR.cellule, VAR.cellule), 0)    
                
                
                self.afficher_faces(element, x, y)
                    
                #image_texte = self.ecriture.render(str(len(self.CORPS.elements) - index), True, (0,0,0)) 
                image_texte = self.ecriture.render(str(element.direction), True, (0,0,0)) 
                VAR.fenetre.blit(image_texte, (xc + ((VAR.cellule - image_texte.get_width()) // 2), yc + ((VAR.cellule - image_texte.get_height()) // 2)))
            
        #xc, yc = self.x * VAR.cellule, self.y * VAR.cellule       
        #pygame.draw.rect(VAR.fenetre, (255, 255, 0), (xc, yc, VAR.cellule, VAR.cellule), 0)    
        
        if not (-1, -1) == (self.CORPS.LIMITE.x, self.CORPS.LIMITE.y): 
            couleur = (0,0,255) if self.CORPS.id_interieur == 1 else (0,128,128)    
            xc, yc = self.CORPS.LIMITE.x * VAR.cellule, self.CORPS.LIMITE.y * VAR.cellule       
            pygame.draw.rect(VAR.fenetre, couleur, (xc, yc, VAR.cellule, VAR.cellule), 4)    
       
        
        