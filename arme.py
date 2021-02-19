import classe as cl

# Cac

morgenstern = cl.Arme(6, 'F', 'F', 0, 0, "morgenstern", 'cac', poids = 3)
poing = cl.Arme(4,'F','F',-2,-1,"poing",'cac')
epee_courte_dex = cl.Arme(8, 'Dex', 'F', 0, 0, "epee courte",'cac',poids = 1)
epee_courte_f = cl.Arme(8, 'F', 'F', 0, 0, "epee courte",'cac',poids =1)
faux = cl.Arme(12,'F','F',2,0,"faux",'cac', poids = 5)
cimeterre = cl.Arme(8,'F','F', 0, 0, 'cimeterre', 'cac', 18, 2)
baton = cl.Arme(6, 'Dex', 'F', 0, 0, 'baton', 'cac',poids = 2)
epee_longue = cl.Arme(8, 'F', 'F', 0, 2, 'epee longue', 'cac', 19, poids = 2)

# bouclier
rien = cl.Bouclier(0,0,'rien', poids = 0)
rondache = cl.Bouclier(1, 0, "rondache", poids = 2)

# Tir

arc_composite = cl.Arme(6,'Dex', None, 1, 0, "arc composite",'tir', poids = 1.5)
javeline = cl.Arme(6, 'Dex', None, 0, 0, "javeline", 'tir', poids = 1)

# Armure

cuir = cl.Armure(2, 0, "cuir",poids = 7.5)
cuir_cloute = cl.Armure(3, 0, "cuir clouté", poids = 10)
cuir_cloute_maitre= cl.Armure(4, 0, "cuir clouté de maître", poids = 10)
crevice = cl.Armure(7,-3, "crevice", poids = 17.5)