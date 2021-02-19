from math import floor
import numpy as np
import random as rd

class Objet():
    def __init__(self, nom, poids, valeur):
        self.nom = nom
        self.poids = poids
        self.valeur = valeur

class Arme():
    def __init__(self, de_degat, carac_touche, carac_degat, bonus_touche = 0, bonus_degat = 0,nom="arme", typ='cac',\
                critique = 20, poids = 0):
        self.de_degat = de_degat
        self.bonus_touche = bonus_touche
        self.bonus_degat = bonus_degat
        self.carac_touche = carac_touche
        self.carac_degat = carac_degat
        self.nom = nom
        self.typ = typ
        self.critique = critique
        self.poids = poids
        
poing = Arme(4,'F','F',-2,-1,"poing",'cac')

class Bouclier():
    def __init__(self, bonus_CA, penalite_dex = 0, nom = "bouclier", typ='bouclier', poids=0):
        self.bonus_CA = bonus_CA
        self.penalite_dex = penalite_dex
        self.nom = nom 
        self.typ = typ
        self.poids = poids
        
rien = Bouclier(0,0,'rien', poids = 0)

class Armure():
    def __init__(self, bonus_CA, penalite_dex = 0, nom = "armure", poids = 0):
        self.bonus_CA = bonus_CA
        self.penalite_dex = penalite_dex
        self.nom = nom 
        self.poids = poids

tenue_lin = Armure(0,0,"tenue de lin")
        
def calcul_CA(armure, bDex, dons):
    if 'armure_legere_1' in dons:
        penalite_dex = min(0,armure.penalite_dex+2)
    elif 'armure_legere_2' in dons:
        penalite_dex = min(0,armure.penalite_dex+4)
    else:
        penalite_dex = armure.penalite_dex
    return 10+ armure.bonus_CA + max(0,bDex + penalite_dex)

def calcul_poids(poids_perso, armure, arme1, arme2, arme3, bouclier, PO):
    return poids_perso + armure.poids + arme1.poids + arme2.poids + arme3.poids + bouclier.poids + PO*0.006

def calcul_charge(poids_total, poids, F):
        if (poids_total-poids) < np.exp(0.87*F**0.52):
            return 'leger'
        elif (poids_total-poids) < np.exp(F**0.52+5):
            return 'intermediaire'
        else:
            return 'lourd'
        
class Equipement():
    def __init__(self, sac = 1, torche = 0, fleche = 0, fleche_composite = 0, ration = 0):
        self.sac = sac
        

class Personnage():
    def __init__(self,F, Dex, Con, Cst, PV, arme1=poing, arme2=poing, arme3=poing, armure=tenue_lin,\
                 bouclier = rien, XP = 0,nom = "PNJ",  Lvl=1, PO = 0, BBA=0,\
                 dons=[], mana = 0, sorts = [], poids = 70, breflex = 0, bvigueur = 0, bvolonte = 0):
        self.dons =dons
        self.F=F
        self.bF = floor((self.F-10)/2)
        self.Dex=Dex
        self.bDex = floor((self.Dex-10)/2)
        self.Con=Con
        self.bCon = floor((self.Con-10)/2)
        self.Cst = Cst
        self.bCst = floor((self.Cst - 10)/2)
        self.PV = PV
        self.PV_max = self.PV
        self.vigueur = self.bCst +bvigueur
        self.reflex = self.bDex + breflex
        self.volonte = self.bCon + bvolonte
        self.arme1 = arme1
        self.arme2 = arme2
        self.arme3 = arme3
        self.bouclier = bouclier
        self.armure = armure
        self.XP = XP
        self.nom = nom
        self.Lvl = Lvl
        self.PO=PO
        self.BBA=BBA
        self.mana = mana
        self.mana_max = mana
        self.CA = calcul_CA(self.armure, self.bDex, self.dons )
        self.sorts = sorts
        self.poids = poids
        self.poids_total = calcul_poids(poids, armure, arme1, arme2, arme3, bouclier, PO)
        self.charge = calcul_charge(self.poids_total,self.poids, self.F)
    
    
        
    def bonus_arme(self, arme, sorte = 'touche'):
        b_t, b_d = arme.bonus_touche, arme.bonus_degat
        if arme.carac_touche == 'Dex':
            b_t+=self.bDex
        elif arme.carac_touche == 'F' :
            b_t+=self.bF
        if arme.carac_degat == 'F':
            b_d+= self.bF
        elif arme.carac_degat == 'Dex':
            b_d+=self.bDex
        if sorte == 'touche':
            return b_t+self.BBA
        else:
            return b_d
    
    def resume(self, full = True):
        print(self.nom + " | PV : " + str(self.PV)+"/"+str(self.PV_max)+ " | PM : " + str(self.mana)+"/"+str(self.mana_max)+" | CA : "+str(self.CA)+"(+"+str(self.bouclier.bonus_CA)+") | Poids : "+str(self.poids_total)+"kg ("+self.charge+")")
        
        print("F : "+str(self.F)+"(+"+str(self.bF)+")"+" | Dex : "+str(self.Dex)+"(+"+str(self.bDex)+")"\
              +" | Con : "+str(self.Con)+"(+"+str(self.bCon)+")"+" | Cst : "+str(self.Cst)+"(+"+str(self.bCst)+\
              ")")
        
        print("Cac1 : "+self.arme1.nom+"("+str(self.bonus_arme(self.arme1))+"/"+str(self.bonus_arme(self.arme1, 'degat')) +"), Cac2 : "+self.arme2.nom+"("+str(self.bonus_arme(self.arme2))+"/"+str(self.bonus_arme(self.arme2, 'degat')) +"), Tir : "+self.arme3.nom+"("+str(self.bonus_arme(self.arme3))+"/"+str(self.bonus_arme(self.arme3, 'degat')) +")")
        print("Armure : "+self.armure.nom)
        
#def modification_personnage(F=-1, Dex=-1, Con=-1, Cst=-1, PV=-1, arme1=-1, arme2=-1, arme3=-1, armure=-1,\
 #                bouclier = -1, XP = -1,nom = -1,  Lvl=-1, PO = -1, BBA=-1,\
  #               dons=-1, mana = -1, sorts = -1, poids = -1, equipement = -1):
   # l_attr=[]
    #for 
    
    