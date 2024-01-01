import pygame, time

from fonctions import *
import variables as VAR

from corps import *
class CJoueur:
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
        for y in range(-2, 2):
            for x in range(-2, 2):
                if 0 <= self.x + x < self.MOTEUR.TERRAIN.dimension_x and 0 <= self.y + y < self.MOTEUR.TERRAIN.dimension_y:
                    self.MOTEUR.TERRAIN.zone[self.x + x][self.y + y] = self
                    self.MOTEUR.JOUEUR.LISTE_ZONES.append( (self.x + x, self.y + y) )
        self.CORPS.regime()
                
                    
    def capture_zone(self):
        t = time.time()
        
        liste_zones_a_explorer = set()
        zones_explorees = set()

        def ajouter_zone(x, y):
            if 0 <= x < self.MOTEUR.TERRAIN.dimension_x and 0 <= y < self.MOTEUR.TERRAIN.dimension_y:
                if self.MOTEUR.TERRAIN.zone[x][y] != self and (x, y) not in zones_explorees:
                    if (x, y) not in self.CORPS.elements:
                        liste_zones_a_explorer.add((x, y))
                  

        # Initialisation des zones à explorer
        
        for coord, element in self.CORPS.elements.items():
            x, y = coord
            for face in self.CORPS.trouve_faces(x, y):
                xd, yd = FACES[face]               
                ajouter_zone(x + xd, y + yd)

        # Propagation
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

            
                
    def se_deplacer(self):
        if time.time() - self.vitesse_timer < self.vitesse:
            return
        
        self.vitesse_timer = time.time()
        xd, yd = FACES[self.direction]
        self.x += xd
        self.y += yd
        
        if not (self.x, self.y) in self.MOTEUR.JOUEUR.LISTE_ZONES:
            if not self.MOTEUR.TERRAIN.zone[self.x][self.y] == self:
                self.CORPS.ajouter_morceau( self.x, self.y )
            
        else:        
            if len(self.CORPS.elements) > 4:
                self.capture_zone()
                self.CORPS.regime()
        
        
    def afficher(self):
               
       
        
        if len(self.CORPS.elements) > 0:
          
            for index, donnees in enumerate(self.CORPS.elements.items()):
                coord, element = donnees            
                x, y = coord
                
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
              
            couleur = (0,0,255) if self.CORPS.id_interieur == 1 else (0,128,128)    
            xc, yc = self.CORPS.LIMITE.x * VAR.cellule, self.CORPS.LIMITE.y * VAR.cellule       
            pygame.draw.rect(VAR.fenetre, couleur, (xc, yc, VAR.cellule, VAR.cellule), 0)    
            pygame.draw.rect(VAR.fenetre, (128, 128, 0), (xc, yc, VAR.cellule, VAR.cellule), 2)   
             
        
        xc, yc = self.x * VAR.cellule, self.y * VAR.cellule       
        pygame.draw.rect(VAR.fenetre, (255, 255, 0), (xc, yc, VAR.cellule, VAR.cellule), 0)    
        
        
        