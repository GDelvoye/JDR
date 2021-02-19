import classe as cl
import arme as ar

import random as rd

#[Nb Dé, Type Dé, Bonus Dé, F, Dex, Con, Cst, arme1, arme2, arme3, armure, nom, Lvl, PO, BBA, dons, mana, sorts]


gobelin = [[1, 8, 1], 11,13, 9, 12, ar.morgenstern, ar.poing, ar.poing, ar.cuir,\
           "gobelin", 1, [1,4,0], 2, [], 0, [], ar.rondache]
hobgobelin = [[1,8,2], 13,13,11,14, ar.epee_longue, ar.poing, ar.javeline, ar.cuir_cloute, \
             "hobgobelin", 1, [1,8,0], 1, [], 0, [], ar.rondache]

#(self,F, Dex, Con, Cst, PV, arme1=poing, arme2=poing, arme3=poing, armure=tenue_lin,\
 #                XP = 0,nom = "PNJ",  Lvl=1, PO = 0, BBA=0,dons=[], mana = 0, sorts = []):
  #      self.dons =dons

def creation_monstre(l):
    PV = 0
    for i in range(0,l[0][0]):
        PV+=rd.randint(1,l[0][1])+l[0][2]
    PO = 0
    for i in range(0,l[11][0]):
        PO+=rd.randint(0,l[11][1])+l[11][2]
    monstre = cl.Personnage(l[1], l[2], l[3], l[4], PV = PV,\
                            arme1 =l[5], arme2 = l[6], arme3 =l[7], armure =l[8],\
                            nom = l[9],Lvl = l[10], PO = PO, BBA = l[12], dons = l[13],\
                            mana=l[14], sorts = l[15], bouclier = l[16])
    return monstre
    
    