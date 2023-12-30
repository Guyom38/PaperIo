import pygame
from pygame.locals import *

import variables as VAR

from algo_flood import *
from terrain import *

class CMoteur:
    def __init__(self):
   
        pygame.init()

        VAR.fenetre = pygame.display.set_mode((VAR.resolution_x, VAR.resolution_y), pygame.DOUBLEBUF, 32)
        pygame.display.set_caption("Paper.Io")

        self.horloge = pygame.time.Clock()

        self.TERRAIN = CTerrain(self)
        self.ALGO_REMPLISSAGE = CAlgo_Remplissage(self)
        

    def demarrer(self):
        VAR.boucle = True
        self.boucle()
        
        
    def boucle(self):
        while VAR.boucle:

            for event in pygame.event.get():       
                
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    VAR.boucle = False
               
                if event.type == KEYDOWN:  
                    if event.key == K_LEFT: print("la touche gauche")
                    if event.key == K_RIGHT: print("la touche droite")
                    if event.key == K_UP: print("la touche haut")
                    if event.key == K_DOWN: print("la touche bas")

           
            VAR.fenetre.fill((16,16,16))
            self.TERRAIN.afficher()
           

            pygame.display.update()
            self.horloge.tick(25)

        pygame.quit() 