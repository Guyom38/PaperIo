import pygame
from pygame.locals import *

import variables as VAR

from algo_flood import *
from terrain import *
from joueur import *
from corps import *

class CMoteur:
    def __init__(self):
   
        pygame.init()

        VAR.fenetre = pygame.display.set_mode((VAR.resolution_x, VAR.resolution_y), pygame.DOUBLEBUF, 32)
        pygame.display.set_caption("Paper.Io")

        self.horloge = pygame.time.Clock()

        self.TERRAIN = CTerrain(self)
        self.JOUEUR = CJoueur(self)
        
    def charger_terrain(self):
        image = pygame.image.load("demo1.png")
        
        for y in range(image.get_height()):
            for x in range(image.get_width()):
                pixel = image.get_at( (x, y) )

                if pixel == (0, 255, 0, 255):
                    self.JOUEUR.LISTE_ZONES.append( (x, y) )
 
        for y in range(image.get_height()):
            for x in range(image.get_width()):
                pixel = image.get_at( (x, y) )

                if pixel == (0, 0, 255, 255): # trouve la tete
                    self.JOUEUR.x, self.JOUEUR.y = x, y 
                    
                    # --- trouve la direction de depart
                    for xd, yd, direction in ( (0, 1, ENUM_DIR.HAUT), (-1, 0, ENUM_DIR.DROITE), (1, 0, ENUM_DIR.GAUCHE), (0, -1, ENUM_DIR.BAS)):
                        if (x + xd, y + yd) in self.JOUEUR.LISTE_ZONES:
                            self.JOUEUR.direction = direction
                            break
            
                    self.JOUEUR.CORPS.ajouter_morceau( x , y)  
 
        
        
            
        x, y = self.JOUEUR.x, self.JOUEUR.y
        pixel = image.get_at( (x, y) )                                
        while not pixel == (255, 0, 0, 255): # trouve le cul
            for xd, yd in ( (0, 1), (1, 0), (0, -1), (-1, 0) ):
                if 0 <= (x + xd) < image.get_width() and 0 <= (y + yd) < image.get_height():
                    pixel = image.get_at( (x + xd, y + yd) ) 
                    if (pixel == (0, 0, 0, 255) or pixel == (255, 0, 0, 255) ) and not (x + xd, y + yd) in self.JOUEUR.CORPS.elements:
                        self.JOUEUR.CORPS.ajouter_morceau( x + xd, y + yd )
                        x, y = x + xd, y + yd
                        break
        
 
        
    def demarrer(self):
        self.JOUEUR.creer_la_zone_de_depart()
        #self.charger_terrain()
        VAR.boucle = True
        self.boucle()
           
    def boucle(self):
        while VAR.boucle:

            for event in pygame.event.get():       
                
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    VAR.boucle = False
               
                if event.type == KEYDOWN:  
                    if event.key == K_LEFT: self.JOUEUR.direction = ENUM_DIR.GAUCHE
                    if event.key == K_RIGHT: self.JOUEUR.direction = ENUM_DIR.DROITE
                    if event.key == K_UP: self.JOUEUR.direction = ENUM_DIR.HAUT
                    if event.key == K_DOWN: self.JOUEUR.direction = ENUM_DIR.BAS
                    if event.key == K_SPACE: self.JOUEUR.direction = ENUM_DIR.AUCUN

            self.JOUEUR.se_deplacer()
            if self.JOUEUR.mort:
                self.JOUEUR.creer_la_zone_de_depart()
                
            
            
            
            self.TERRAIN.afficher()
            self.JOUEUR.afficher(1)
           # self.JOUEUR.capture_zone()
           

            pygame.display.update()
            self.horloge.tick(25)

        pygame.quit() 