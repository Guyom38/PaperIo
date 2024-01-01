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
                    self.face[ENUM_DIR.HAUT] = 3
                    
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
    def __init__(self, x, y, dim_x, dim_y):
        # Initialement, la référence est définie à une valeur élevée pour être sûre qu'elle sera mise à jour
        self.reference = -1
        self.face = ENUM_DIR.AUCUN
        
        self.x, self.y = x, y
        self.ref_x, self.ref_y = x, y
        
        self.dimension_x, self.dimension_y = dim_x, dim_y
       
    
    def controle(self, x, y):
        # Calcul des distances par rapport à chaque bord
        distances = {
            ENUM_DIR.HAUT: x,
            ENUM_DIR.BAS: self.dimension_x - x,
            ENUM_DIR.GAUCHE: y,
            ENUM_DIR.DROITE: self.dimension_y - y
        }
        
        cle, distance_bord = min(distances.items(), key=lambda item: item[1])
        distance = calculer_distance( (x, y), (self.ref_x, self.ref_y) ) 
       
        if distance > self.reference:                
                self.reference = distance
                self.x, self.y = x, y
                self.face = cle
            
  
                
      
            
            
class CCorps:
    def __init__(self, moteur):
        self.MOTEUR = moteur
        self.elements = {}    
        self.id_interieur = 0
        self.LIMITE = CBord(-1, -1, -1, -1)
      
    def regime(self):   
        self.elements = {}    
        self.id_interieur = 0
        self.LIMITE = CBord(-1, -1, self.MOTEUR.TERRAIN.dimension_x, self.MOTEUR.TERRAIN.dimension_y)  
        
       
    def ajouter_morceau(self, x, y):
        dernier_morceau = None
        direction = ENUM_DIR.AUCUN
        
        if len(self.elements) > 0:
            dernier_morceau = list(self.elements.values())[-1]
            
            xD, yD = dernier_morceau.x, dernier_morceau.y            
            if direction == ENUM_DIR.AUCUN:
                if x > xD: direction = ENUM_DIR.DROITE
                elif x < xD: direction = ENUM_DIR.GAUCHE
                elif y > yD: direction = ENUM_DIR.BAS
                elif y < yD: direction = ENUM_DIR.HAUT
                
        else:
            direction = self.MOTEUR.JOUEUR.direction
            
        nouveau_morceau = CMorceau(x, y, direction, dernier_morceau)       
        self.elements[(x, y)] = nouveau_morceau
        
        self.LIMITE.controle(x, y)        
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

        
        
        
        