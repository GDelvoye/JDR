import random as rd

def attaque(personnage, arme, simul = False):
    #bonus de touche
    bonus_touche = personnage.BBA
    if arme.carac_touche == 'F':
        bonus_touche += personnage.bF
    elif arme.carac_touche == 'Dex':
        bonus_touche+= personnage.bDex
    bonus_touche+=arme.bonus_touche
    #bonus de degat
    bonus_degat = arme.bonus_degat
    if arme.carac_degat == 'F':
        bonus_degat += personnage.bF
    elif arme.carac_degat == 'Dex':
        bonus_degat += personnage.bDex
    if simul == True:
        touche = rd.randint(1,20)
        touche+=bonus_touche
        degat = rd.randint(1,arme.de_degat)
        if degat >= arme.critique:
            cc=True
            degat+=rd.randint(1,arme.de_degat)
        degat+=bonus_degat
        cc=False
        return touche, degat, cc
    return "+"+str(bonus_touche), 'D'+str(arme.de_degat)+"+"+str(bonus_degat)

def combat_round(p1, p2, a1 = [1],a2 = [1]):
    for i in a1:
        if i==1:
            a = p1.arme1
        elif i==2:
            a=p1.arme2
        elif i==3:
            a=p1.arme3
        t1, d1, cc = attaque(p1, a, True)
        if t1 > p2.CA or cc==True:
            p2.PV -= d1
    if p2.PV >0:
        for i in a2:
            if i==1:
                a = p2.arme1
            elif i==2:
                a=p2.arme2
            elif i==3:
                a=p2.arme3
        t2,d2, cc = attaque(p2,a,True)
        if t2 > p1.CA or cc == True:
            p1.PV -= d2
            
def combat(p1,p2,a1=[1],a2=[1]):
    pv1, pv2 = p1.PV,p2.PV
    c=0
    while p1.PV >0 and p2.PV >0:
        if 'maitrise_arme' in p1.dons and c%2==0:
            if 'maitrise_arme' in p2.dons and c%2==0:
                combat_round(p1, p2, a1+[1], a2+[1])
            else:
                combat_round(p1, p2, a1+[1], a2)
        elif 'maitrise_arme' in p2.dons and c%2==0:
            combat_round(p1, p2, a1, a2+[1])
        else:
            combat_round(p1, p2, a1, a2)
        c+=1
        
    if p1.PV > 0:
        v=1
        r = p1.PV
    else:
        v=0
        r=p2.PV
    p1.PV=pv1
    p2.PV = pv2
    return c, v, r

def monte_carlo_combat(n,p1,p2,a1=[1],a2=[1],duree=True):
    c=0
    for i in range(0,n):
        d,v,r = combat(p1,p2,a1,a2)
        if duree==True:
            c+=d
        else:
            c+=v
    return c/n