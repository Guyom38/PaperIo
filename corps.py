from constantes import *
import math
import variables as VAR

class CMorceau:
    def __init__(self, x, y, direction, morceau_precedent):
        self.x = x
        self.y = y
        self.direction = direction
        
        self.face = {   ENUM_DIR.BAS : 0, 
                        ENUM_DIR.GAUCHE : 0, 
                        ENUM_DIR.DROITE : 0, 
                        ENUM_DIR.HAUT : 0,
                        ENUM_DIR.CACHE : 0 }

        def autre_cote(valeur):
            if valeur == 0: return 0
            if valeur == 1: return 2
            if valeur == 2: return 1
            
            
        # 0 -> lien entre morceau
        # 1 -> cote 1
        # 2 -> cote 2
        # 3 -> indefini pour l'instant
          
        if not morceau_precedent == None:                  
            mp_droite, mp_gauche, mp_haut, mp_bas = morceau_precedent.face[ENUM_DIR.DROITE], morceau_precedent.face[ENUM_DIR.GAUCHE], morceau_precedent.face[ENUM_DIR.HAUT], morceau_precedent.face[ENUM_DIR.BAS]
            
            # --- Direction Précédente vers le haut
            if morceau_precedent.direction == ENUM_DIR.HAUT:
                if self.direction == ENUM_DIR.HAUT: # 4
                    morceau_precedent.face[ENUM_DIR.HAUT] = 0
                    
                    self.face[ENUM_DIR.BAS] = 0
                    self.face[ENUM_DIR.GAUCHE] = mp_gauche
                    self.face[ENUM_DIR.DROITE] = mp_droite
                    self.face[ENUM_DIR.HAUT] = mp_haut
                    
                elif self.direction == ENUM_DIR.DROITE: # 7
                    morceau_precedent.face[ENUM_DIR.DROITE] = 0
                    morceau_precedent.face[ENUM_DIR.HAUT] = mp_gauche
                    
                    # 8
                    self.face[ENUM_DIR.BAS] = mp_droite
                    self.face[ENUM_DIR.GAUCHE] = 0
                    self.face[ENUM_DIR.DROITE] = 3
                    self.face[ENUM_DIR.HAUT] = mp_gauche
                    
                elif self.direction == ENUM_DIR.GAUCHE: # 9
                    morceau_precedent.face[ENUM_DIR.GAUCHE] = 0
                    morceau_precedent.face[ENUM_DIR.HAUT] = mp_droite
                    
                    # 8
                    self.face[ENUM_DIR.BAS] = mp_gauche
                    self.face[ENUM_DIR.GAUCHE] = 3
                    self.face[ENUM_DIR.DROITE] = 0
                    self.face[ENUM_DIR.HAUT] = mp_droite
                    
            # --- Direction Précédente vers la droite
            elif morceau_precedent.direction == ENUM_DIR.DROITE:
                if self.direction == ENUM_DIR.DROITE:
                    morceau_precedent.face[ENUM_DIR.DROITE] = 0
                    morceau_precedent.face[ENUM_DIR.HAUT] = mp_haut
                    
                    self.face[ENUM_DIR.BAS] = mp_bas
                    self.face[ENUM_DIR.GAUCHE] = 0
                    self.face[ENUM_DIR.DROITE] = 3
                    self.face[ENUM_DIR.HAUT] = mp_haut
                    
                elif self.direction == ENUM_DIR.BAS:
                    morceau_precedent.face[ENUM_DIR.BAS] = 0
                    morceau_precedent.face[ENUM_DIR.DROITE] = mp_haut
                    
                    self.face[ENUM_DIR.BAS] = 3
                    self.face[ENUM_DIR.GAUCHE] = autre_cote(mp_haut)
                    self.face[ENUM_DIR.DROITE] = mp_haut
                    self.face[ENUM_DIR.HAUT] = 0
                    
                elif self.direction == ENUM_DIR.HAUT:
                    morceau_precedent.face[ENUM_DIR.HAUT] = 0
                    morceau_precedent.face[ENUM_DIR.DROITE] = mp_bas
                    
                    self.face[ENUM_DIR.BAS] = 0
                    self.face[ENUM_DIR.GAUCHE] = mp_haut
                    self.face[ENUM_DIR.DROITE] = mp_bas
                    self.face[ENUM_DIR.HAUT] = 3
                    
            # --- Direction Précédente vers le bas        
            elif morceau_precedent.direction == ENUM_DIR.BAS:
                if self.direction == ENUM_DIR.BAS:
                    morceau_precedent.face[ENUM_DIR.BAS] = 0
                     
                    self.face[ENUM_DIR.BAS] = 3
                    self.face[ENUM_DIR.GAUCHE] = mp_gauche
                    self.face[ENUM_DIR.DROITE] = mp_droite
                    self.face[ENUM_DIR.HAUT] = 0
                    
                elif self.direction == ENUM_DIR.DROITE:
                    morceau_precedent.face[ENUM_DIR.DROITE] = 0
                    morceau_precedent.face[ENUM_DIR.BAS] = mp_gauche
                     
                    self.face[ENUM_DIR.BAS] = mp_gauche
                    self.face[ENUM_DIR.GAUCHE] = 0
                    self.face[ENUM_DIR.DROITE] = 3
                    self.face[ENUM_DIR.HAUT] = mp_droite
                    
                elif self.direction == ENUM_DIR.GAUCHE:
                    morceau_precedent.face[ENUM_DIR.GAUCHE] = 0
                    morceau_precedent.face[ENUM_DIR.BAS] = mp_droite
                    
                    self.face[ENUM_DIR.BAS] = mp_droite
                    self.face[ENUM_DIR.GAUCHE] = 3
                    self.face[ENUM_DIR.DROITE] = 0
                    self.face[ENUM_DIR.HAUT] = autre_cote(mp_droite)
                    
            # --- Direction Précédente vers la gauche        
            elif morceau_precedent.direction == ENUM_DIR.GAUCHE:
                if self.direction == ENUM_DIR.BAS:
                    morceau_precedent.face[ENUM_DIR.BAS] = 0
                    morceau_precedent.face[ENUM_DIR.GAUCHE] = mp_haut
                     
                    self.face[ENUM_DIR.BAS] = 3
                    self.face[ENUM_DIR.GAUCHE] = mp_haut
                    self.face[ENUM_DIR.DROITE] = mp_bas
                    self.face[ENUM_DIR.HAUT] = 0
                    
                elif self.direction == ENUM_DIR.GAUCHE:
                    morceau_precedent.face[ENUM_DIR.GAUCHE] = 0
                     
                    self.face[ENUM_DIR.BAS] = mp_bas
                    self.face[ENUM_DIR.GAUCHE] = 3
                    self.face[ENUM_DIR.DROITE] = 0
                    self.face[ENUM_DIR.HAUT] = mp_haut
                
                elif self.direction == ENUM_DIR.HAUT:
                    morceau_precedent.face[ENUM_DIR.HAUT] = 0
                    morceau_precedent.face[ENUM_DIR.GAUCHE] = mp_bas
                     
                    self.face[ENUM_DIR.BAS] = 0
                    self.face[ENUM_DIR.GAUCHE] = mp_bas
                    self.face[ENUM_DIR.DROITE] = mp_haut
                    self.face[ENUM_DIR.HAUT] = 3
                    
        else:
            if direction == ENUM_DIR.HAUT:
                self.face[ENUM_DIR.BAS] = 0
                self.face[ENUM_DIR.GAUCHE] = 1
                self.face[ENUM_DIR.DROITE] = 2
                self.face[ENUM_DIR.HAUT] = 3    
                    
class CBord:
    def __init__(self):
        # Initialement, la référence est définie à une valeur élevée pour être sûre qu'elle sera mise à jour
        self.reference = float('inf')
    
    def controle(self, x, y, dim_x, dim_y):
        # Calcul des distances par rapport à chaque bord
        x_haut = x
        x_bas = dim_x - x
        y_gauche = y
        y_droite = dim_y - y
        
        # Trouver la distance minimale parmi les quatre
        self.reference = min(x_haut, x_bas, y_gauche, y_droite)
        
class CCorps:
    def __init__(self):
        self.elements = []
        self.elements_id = []
        
        self.LIMITE = CBord()
        
    def ajouter_morceau(self, x, y, direction = ENUM_DIR.AUCUN):
        dernier_morceau = None
        if len(self.elements) > 0:
            dernier_morceau = self.elements[-1]
            
            xD, yD = dernier_morceau.x, dernier_morceau.y
            
            if direction == ENUM_DIR.AUCUN:
                if x > xD: direction = ENUM_DIR.DROITE
                elif x < xD: direction = ENUM_DIR.GAUCHE
                elif y > yD: direction = ENUM_DIR.BAS
                elif y < yD: direction = ENUM_DIR.HAUT
                else:
                    direction = ENUM_DIR.AUCUN
    
            
        nouveau_morceau = CMorceau(x, y, direction, dernier_morceau)
        self.elements.append(nouveau_morceau)
        self.elements_id.append( (x, y) )
        
        
        
        