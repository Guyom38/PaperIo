from constantes import *
import math
import variables as VAR
from fonctions import *

class CMorceau:
    def __init__(self, x, y, direction, morceau_precedent):
        self.x = x
        self.y = y
        self.direction = direction
        
        self.face = {dir: 0 for dir in [ENUM_DIR.BAS, ENUM_DIR.GAUCHE, ENUM_DIR.DROITE, ENUM_DIR.HAUT]}

        
            
            
        # 0 -> lien entre morceau
        # 1 -> cote 1
        # 2 -> cote 2
        # 3 -> indefini pour l'instant
          
        if not morceau_precedent == None:
            face_ref = morceau_precedent.face.copy()                  
            morceau_precedent.face[self.direction] = 0 
            # --- Direction Précédente vers le haut
            if morceau_precedent.direction == ENUM_DIR.HAUT:
                if self.direction == ENUM_DIR.HAUT: # 4
                    #morceau_precedent.face[ENUM_DIR.HAUT] = 0
                    
                    self.face[ENUM_DIR.BAS] = 0
                    self.face[ENUM_DIR.GAUCHE] = face_ref[ENUM_DIR.GAUCHE]
                    self.face[ENUM_DIR.DROITE] = face_ref[ENUM_DIR.DROITE]
                    self.face[ENUM_DIR.HAUT] = face_ref[ENUM_DIR.HAUT]
                    
                elif self.direction == ENUM_DIR.DROITE: # 7
                    #morceau_precedent.face[ENUM_DIR.DROITE] = 0
                    morceau_precedent.face[ENUM_DIR.HAUT] = face_ref[ENUM_DIR.GAUCHE]
                    
                    # 8
                    self.face[ENUM_DIR.BAS] = face_ref[ENUM_DIR.DROITE]
                    self.face[ENUM_DIR.GAUCHE] = 0
                    self.face[ENUM_DIR.DROITE] = 3
                    self.face[ENUM_DIR.HAUT] = face_ref[ENUM_DIR.GAUCHE]
                    
                elif self.direction == ENUM_DIR.GAUCHE: # 9
                    #morceau_precedent.face[ENUM_DIR.GAUCHE] = 0
                    morceau_precedent.face[ENUM_DIR.HAUT] = face_ref[ENUM_DIR.DROITE]
                    
                    # 8
                    self.face[ENUM_DIR.BAS] = face_ref[ENUM_DIR.GAUCHE]
                    self.face[ENUM_DIR.GAUCHE] = 3
                    self.face[ENUM_DIR.DROITE] = 0
                    self.face[ENUM_DIR.HAUT] = face_ref[ENUM_DIR.DROITE]
                    
            # --- Direction Précédente vers la droite
            elif morceau_precedent.direction == ENUM_DIR.DROITE:
                if self.direction == ENUM_DIR.DROITE:
                    #morceau_precedent.face[ENUM_DIR.DROITE] = 0
                    morceau_precedent.face[ENUM_DIR.HAUT] = face_ref[ENUM_DIR.HAUT]
                    
                    self.face[ENUM_DIR.BAS] = face_ref[ENUM_DIR.BAS]
                    self.face[ENUM_DIR.GAUCHE] = 0
                    self.face[ENUM_DIR.DROITE] = 3
                    self.face[ENUM_DIR.HAUT] = face_ref[ENUM_DIR.HAUT]
                    
                elif self.direction == ENUM_DIR.BAS:
                    #morceau_precedent.face[ENUM_DIR.BAS] = 0
                    morceau_precedent.face[ENUM_DIR.DROITE] = face_ref[ENUM_DIR.HAUT]
                    
                    self.face[ENUM_DIR.BAS] = 3
                    self.face[ENUM_DIR.GAUCHE] = autre_cote(face_ref[ENUM_DIR.HAUT])
                    self.face[ENUM_DIR.DROITE] = face_ref[ENUM_DIR.HAUT]
                    self.face[ENUM_DIR.HAUT] = 0
                    
                elif self.direction == ENUM_DIR.HAUT:
                    #morceau_precedent.face[ENUM_DIR.HAUT] = 0
                    morceau_precedent.face[ENUM_DIR.DROITE] = face_ref[ENUM_DIR.BAS]
                    
                    self.face[ENUM_DIR.BAS] = 0
                    self.face[ENUM_DIR.GAUCHE] = face_ref[ENUM_DIR.HAUT]
                    self.face[ENUM_DIR.DROITE] = face_ref[ENUM_DIR.BAS]
                    self.face[ENUM_DIR.HAUT] = 3
                    
            # --- Direction Précédente vers le bas        
            elif morceau_precedent.direction == ENUM_DIR.BAS:
                if self.direction == ENUM_DIR.BAS:
                    #morceau_precedent.face[ENUM_DIR.BAS] = 0
                     
                    self.face[ENUM_DIR.BAS] = 3
                    self.face[ENUM_DIR.GAUCHE] = face_ref[ENUM_DIR.GAUCHE]
                    self.face[ENUM_DIR.DROITE] = face_ref[ENUM_DIR.DROITE]
                    self.face[ENUM_DIR.HAUT] = 0
                    
                elif self.direction == ENUM_DIR.DROITE:
                    #morceau_precedent.face[ENUM_DIR.DROITE] = 0
                    morceau_precedent.face[ENUM_DIR.BAS] = face_ref[ENUM_DIR.GAUCHE]
                     
                    self.face[ENUM_DIR.BAS] = face_ref[ENUM_DIR.GAUCHE]
                    self.face[ENUM_DIR.GAUCHE] = 0
                    self.face[ENUM_DIR.DROITE] = 3
                    self.face[ENUM_DIR.HAUT] = face_ref[ENUM_DIR.DROITE]
                    
                elif self.direction == ENUM_DIR.GAUCHE:
                    #morceau_precedent.face[ENUM_DIR.GAUCHE] = 0
                    morceau_precedent.face[ENUM_DIR.BAS] = face_ref[ENUM_DIR.DROITE]
                    
                    self.face[ENUM_DIR.BAS] = face_ref[ENUM_DIR.DROITE]
                    self.face[ENUM_DIR.GAUCHE] = 3
                    self.face[ENUM_DIR.DROITE] = 0
                    self.face[ENUM_DIR.HAUT] = autre_cote(face_ref[ENUM_DIR.DROITE])
                    
            # --- Direction Précédente vers la gauche        
            elif morceau_precedent.direction == ENUM_DIR.GAUCHE:
                if self.direction == ENUM_DIR.BAS:
                    #morceau_precedent.face[ENUM_DIR.BAS] = 0
                    morceau_precedent.face[ENUM_DIR.GAUCHE] = face_ref[ENUM_DIR.HAUT]
                     
                    self.face[ENUM_DIR.BAS] = 3
                    self.face[ENUM_DIR.GAUCHE] = face_ref[ENUM_DIR.HAUT]
                    self.face[ENUM_DIR.DROITE] = face_ref[ENUM_DIR.BAS]
                    self.face[ENUM_DIR.HAUT] = 0
                    
                elif self.direction == ENUM_DIR.GAUCHE:
                    #morceau_precedent.face[ENUM_DIR.GAUCHE] = 0
                     
                    self.face[ENUM_DIR.BAS] = face_ref[ENUM_DIR.BAS]
                    self.face[ENUM_DIR.GAUCHE] = 3
                    self.face[ENUM_DIR.DROITE] = 0
                    self.face[ENUM_DIR.HAUT] = face_ref[ENUM_DIR.HAUT]
                
                elif self.direction == ENUM_DIR.HAUT:
                    #morceau_precedent.face[ENUM_DIR.HAUT] = 0
                    morceau_precedent.face[ENUM_DIR.GAUCHE] = face_ref[ENUM_DIR.BAS]
                     
                    self.face[ENUM_DIR.BAS] = 0
                    self.face[ENUM_DIR.GAUCHE] = face_ref[ENUM_DIR.BAS]
                    self.face[ENUM_DIR.DROITE] = face_ref[ENUM_DIR.HAUT]
                    self.face[ENUM_DIR.HAUT] = 3
                    
        else:
            self.face[direction] = 3
            
            if direction == ENUM_DIR.HAUT:
                self.face[ENUM_DIR.BAS] = 0
                self.face[ENUM_DIR.GAUCHE] = 1
                self.face[ENUM_DIR.DROITE] = 2
                
            elif direction == ENUM_DIR.BAS:
                self.face[ENUM_DIR.HAUT] = 0
                self.face[ENUM_DIR.GAUCHE] = 1
                self.face[ENUM_DIR.DROITE] = 2
                
            elif direction == ENUM_DIR.DROITE:
                self.face[ENUM_DIR.GAUCHE] = 0
                self.face[ENUM_DIR.HAUT] = 1
                self.face[ENUM_DIR.BAS] = 2
                
            elif direction == ENUM_DIR.GAUCHE:
                self.face[ENUM_DIR.DROITE] = 0
                self.face[ENUM_DIR.HAUT] = 1
                self.face[ENUM_DIR.BAS] = 2

                    
class CBord:
    def __init__(self):
        # Initialement, la référence est définie à une valeur élevée pour être sûre qu'elle sera mise à jour
        self.reference = float('inf')
        self.face = ENUM_DIR.AUCUN
        self.x, self.y = 0, 0
    
    def controle(self, x, y, dim_x, dim_y):
        # Calcul des distances par rapport à chaque bord
        distances = {
            ENUM_DIR.HAUT: x,
            ENUM_DIR.BAS: dim_x - x,
            ENUM_DIR.GAUCHE: y,
            ENUM_DIR.DROITE: dim_y - y
        }
        
        for key, value in distances.items():
            if value < self.reference:
                self.reference = value
                self.x, self.y = x, y
                self.face = key
      
            
            
class CCorps:
    def __init__(self, moteur):
        self.MOTEUR = moteur
        
        
      
    def regime(self):
        self.elements = {}        
        self.LIMITE = CBord()        
        self.id_interieur = 0
        
        self.ajouter_morceau( self.MOTEUR.JOUEUR.x , self.MOTEUR.JOUEUR.y, ENUM_DIR.HAUT)  
      
        
    def ajouter_morceau(self, x, y, direction = ENUM_DIR.AUCUN):
        dernier_morceau = None
        
        if len(self.elements) > 0:
            dernier_morceau = list(self.elements.values())[-1]
            
            xD, yD = dernier_morceau.x, dernier_morceau.y            
            if direction == ENUM_DIR.AUCUN:
                if x > xD: direction = ENUM_DIR.DROITE
                elif x < xD: direction = ENUM_DIR.GAUCHE
                elif y > yD: direction = ENUM_DIR.BAS
                elif y < yD: direction = ENUM_DIR.HAUT
                else:
                    direction = ENUM_DIR.AUCUN
    
            
        nouveau_morceau = CMorceau(x, y, direction, dernier_morceau)
        self.elements[(x, y)] = nouveau_morceau
        
        self.LIMITE.controle(x, y, self.MOTEUR.TERRAIN.dimension_x, self.MOTEUR.TERRAIN.dimension_y)        
        self.id_interieur = self.trouve_face_interieur()
        
    
    def trouve_faces(self, x, y):
        faces = []
        for face, id in self.elements[ (x, y) ].face.items():
            if id == self.id_interieur:
                faces.append(face)
        return faces
            
            
        
    def trouve_face_interieur(self):
        element_le_plus_proche_du_bord = self.elements[ (self.LIMITE.x, self.LIMITE.y) ]
        id_cote = element_le_plus_proche_du_bord.face[self.LIMITE.face]
        autre_id_cote = autre_cote(id_cote)
        return autre_id_cote

        
        
        
        