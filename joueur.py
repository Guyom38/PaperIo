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
        self.id = 1
        
        self.couleur = VAR.couleur[self.id]
        self.couleur_corps = VAR.couleur_corps[self.id]
        self.couleur_tete = VAR.couleur_tete[self.id]
        self.couleur_angle = VAR.couleur_angle[self.id]
        
        self.ecriture8 = pygame.font.SysFont('arial', 8) 
        self.ecriture = pygame.font.SysFont('arial', 10) 
        self.ecriture30 = pygame.font.SysFont('arial', 30) 
        self.vitesse = 0.1
        self.vitesse_timer = time.time()
        self.mort = False
        
        self.CORPS = CCorps(moteur)
        self.LISTE_ZONES = []
        self.images = {}
        
    def generation_bouts_corps(self):
        image_tmp = pygame.Surface( (VAR.cellule, VAR.cellule), pygame.SRCALPHA)
        pygame.draw.rect(image_tmp, self.couleur_corps, (0, 0, VAR.cellule, VAR.cellule), 0)
        self.images['corps'] = image_tmp
        
        image_tmp1 = pygame.Surface( (VAR.cellule, VAR.cellule), pygame.SRCALPHA)
        pygame.draw.polygon(image_tmp1, self.couleur_angle, ( (VAR.cellule, 0), (VAR.cellule, VAR.cellule), (0, VAR.cellule)), 0)
        self.images['angle7'] = image_tmp1
        self.images['angle9'] = pygame.transform.rotate(image_tmp1, 90)
        self.images['angle3'] = pygame.transform.rotate(image_tmp1, 180)
        self.images['angle1'] = pygame.transform.rotate(image_tmp1, 270)
        
        image_tmp2 = pygame.Surface( (VAR.cellule, VAR.cellule + VAR.taille_tete), pygame.SRCALPHA)
        pygame.draw.rect(image_tmp2, self.couleur_tete, (0, 0, VAR.cellule, VAR.cellule), 0)
        pygame.draw.rect(image_tmp2, self.couleur, (0, VAR.cellule, VAR.cellule, VAR.taille_tete), 0)
        self.images['tete'] = image_tmp2    
        
        
            
    def creer_la_zone_de_depart(self):
        self.generation_bouts_corps()
        
        self.CORPS = CCorps(self.MOTEUR)
        self.LISTE_ZONES = []
        self.mort = False
        
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
                
                    
    

            
    def se_mord_la_queue(self):
        return (self.x, self.y) in self.CORPS.elements  
            
    def se_deplacer(self):
        if time.time() - self.vitesse_timer < self.vitesse:
            return
        
        if self.direction == ENUM_DIR.AUCUN:
            return
        
        self.vitesse_timer = time.time()
        xd, yd = FACES[self.direction]
        self.x += xd
        self.y += yd
        
        if self.se_mord_la_queue():
            self.mort = True
            return
        
        if not (self.x, self.y) in self.LISTE_ZONES:
            self.CORPS.ajouter_morceau( self.x, self.y )
            
        else:        
            if len(self.CORPS.elements) > 1:
                self.CORPS.id_interieur = self.CORPS.trouve_face_interieur()
        
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
           
       
        
    def afficher(self, i):
        if i == 0:
            cles = list(self.CORPS.elements.keys())  
            cles.append( (self.x, self.y))        
            for index, coord in enumerate(cles):           
                bout_x, bout_y = coord

                if index < len(cles)-1:
                    devant_x, devant_y = cles[index+1]
                    derriere_x, derriere_y = (-1, -1) if index-1 < 0 else cles[index-1]
                    
                    sens_derriere = ENUM_DIR.AUCUN
                    if derriere_x > -1 or derriere_y > -1:
                        if derriere_x < bout_x: sens_derriere = ENUM_DIR.DROITE
                        elif derriere_x > bout_x: sens_derriere = ENUM_DIR.GAUCHE
                        elif derriere_y < bout_y: sens_derriere = ENUM_DIR.BAS
                        elif derriere_y > bout_y: sens_derriere = ENUM_DIR.HAUT
                        
                    sens_devant = ENUM_DIR.AUCUN
                    if devant_x > bout_x: sens_devant = ENUM_DIR.DROITE
                    elif devant_x < bout_x: sens_devant = ENUM_DIR.GAUCHE
                    elif devant_y > bout_y: sens_devant = ENUM_DIR.BAS
                    elif devant_y < bout_y: sens_devant = ENUM_DIR.HAUT
                    
                    image = self.images['corps']
                    if sens_derriere == ENUM_DIR.DROITE: 
                        if sens_devant == ENUM_DIR.BAS: 
                            image = self.images['angle1']
                        elif sens_devant == ENUM_DIR.HAUT: 
                            image = self.images['angle3']
                    elif sens_derriere == ENUM_DIR.GAUCHE: 
                        if sens_devant == ENUM_DIR.BAS: 
                            image = self.images['angle7']
                        elif sens_devant == ENUM_DIR.HAUT: 
                            image = self.images['angle9']
                    elif sens_derriere == ENUM_DIR.HAUT: 
                        if sens_devant == ENUM_DIR.DROITE: 
                            image = self.images['angle7']
                        elif sens_devant == ENUM_DIR.GAUCHE: 
                            image = self.images['angle1']
                    elif sens_derriere == ENUM_DIR.BAS: 
                        if sens_devant == ENUM_DIR.DROITE: 
                            image = self.images['angle9']
                        elif sens_devant == ENUM_DIR.GAUCHE: 
                            image = self.images['angle3']
                            
                    offset_y = 0

                else:
                    image = self.images['tete']
                    offset_y = VAR.taille_tete
                
                x, y = (bout_x * VAR.cellule),  (bout_y * VAR.cellule) - offset_y
                VAR.fenetre.blit( image, (x, y) )
            
        else:    
            self.CORPS.id_interieur = self.CORPS.trouve_face_interieur()
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

                    
            xc, yc = self.x * VAR.cellule, self.y * VAR.cellule       
            pygame.draw.rect(VAR.fenetre, (255, 255, 0), (xc, yc, VAR.cellule, VAR.cellule), 0)    

            if not (-1, -1) == (self.CORPS.LIMITE.x, self.CORPS.LIMITE.y): 
                couleur = (0,0,255) if self.CORPS.id_interieur == 1 else (0,128,128)    
                xc, yc = self.CORPS.LIMITE.x * VAR.cellule, self.CORPS.LIMITE.y * VAR.cellule       
                pygame.draw.rect(VAR.fenetre, couleur, (xc, yc, VAR.cellule, VAR.cellule), 8)    
                
                d = 4
                if self.CORPS.LIMITE.face == ENUM_DIR.DROITE:
                    pygame.draw.rect(VAR.fenetre, (0, 0, 255), (xc+ VAR.cellule-d, yc, d, VAR.cellule), 0)   
                elif self.CORPS.LIMITE.face == ENUM_DIR.GAUCHE:
                    pygame.draw.rect(VAR.fenetre, (0, 0, 255), (xc, yc, d, VAR.cellule), 0)   
                elif self.CORPS.LIMITE.face == ENUM_DIR.HAUT:
                    pygame.draw.rect(VAR.fenetre, (0, 0, 255), (xc, yc, VAR.cellule, d), 0)   
                elif self.CORPS.LIMITE.face == ENUM_DIR.BAS:
                    pygame.draw.rect(VAR.fenetre, (0, 0, 255), (xc, yc+VAR.cellule-d, VAR.cellule, d), 0)   
                
                if self.CORPS.id_interieur in (1, 2):  
                    image_texte = self.ecriture30.render("INTERIEUR" + str(self.CORPS.id_interieur), True, couleur, (32, 32, 32)) 
                    VAR.fenetre.blit(image_texte, (0, 0))
       
        
        