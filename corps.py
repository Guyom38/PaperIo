from constantes import *
import math
import variables as VAR
from fonctions import *

class CMorceau:
    def rotation(self, faces):
            self.face[ENUM_DIR.HAUT] = faces[ENUM_DIR.DROITE]
            self.face[ENUM_DIR.DROITE] = faces[ENUM_DIR.BAS]
            self.face[ENUM_DIR.BAS] = faces[ENUM_DIR.GAUCHE]
            self.face[ENUM_DIR.GAUCHE] = faces[ENUM_DIR.HAUT]
            
        
        
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
                    self.coin = True
                    
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
        self.reference = -1
        self.face = ENUM_DIR.AUCUN
        self.coin = False
        
        self.x, self.y = x, y
        self.ref_x, self.ref_y = x, y
        self.dimension_x, self.dimension_y = dim_x, dim_y

    def controle(self, x, y):
        # Calcul des distances par rapport à chaque bord
        distances = {
            ENUM_DIR.HAUT: y,
            ENUM_DIR.BAS: self.dimension_y - y,
            ENUM_DIR.GAUCHE: x,
            ENUM_DIR.DROITE: self.dimension_x - x
        }

        # Trouver le bord le plus proche
        cle, distance_bord = min(distances.items(), key=lambda item: item[1])

        # Calculer la distance euclidienne par rapport au point de référence
        distance = calculer_distance((x, y), (self.ref_x, self.ref_y))

        if distance > self.reference:
            self.reference = distance
            self.x, self.y = x, y
            self.face = cle
            print(str( ((self.ref_x, self.ref_y), (x, y), distance, cle)))
            
            
            
  
                
      
            
            
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
            self.LIMITE = CBord(x, y, self.MOTEUR.TERRAIN.dimension_x, self.MOTEUR.TERRAIN.dimension_y)  
            
        nouveau_morceau = CMorceau(x, y, direction, dernier_morceau)       
        self.elements[(x, y)] = nouveau_morceau
        
        self.LIMITE.controle(x, y)        
        
        

            
            
        
    def trouve_face_interieur(self):
        if (self.LIMITE.x, self.LIMITE.y) == (-1, -1):
            return 0
        
        bord = self.elements[ (self.LIMITE.x, self.LIMITE.y) ]
        id_cote = bord.face[self.LIMITE.face]
        
        if id_cote == 0:
            for _, valeur in bord.face.items():
                if valeur in (1, 2):
                    id_cote = valeur
                    break
                
        bord_oppose = autre_cote(id_cote)
        if bord_oppose == 0:
            print( str( (self.LIMITE.x, self.LIMITE.y, self.elements[(self.LIMITE.x, self.LIMITE.y)])) )
            raise ExceptionType("L'interieur n'a pas été déterminé.")  
        
        return bord_oppose

        
        
        
        