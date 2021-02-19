import classe as cl
import arme as ar

elrosgarius = cl.Personnage(12,16,12,12,PV=29,arme3=ar.arc_composite, arme2=ar.epee_courte_dex,\
                            arme1=ar.epee_courte_dex,armure=ar.cuir_cloute,\
                         nom="Elrosgarius", Lvl=4, PO=337, BBA=2,\
                        dons=['tir_lointain'])

ysoria = cl.Personnage(16,14,9,14,PV=45,arme1=ar.faux, armure=ar.crevice,\
                    nom="Ysoria", Lvl=4, PO=334.5, BBA=3,\
                    dons=['armure_legere_1','maitrise_arme','saignement','attaque_circulaire'])

neven = cl.Personnage(11, 12, 16, 10, 22, ar.epee_courte_f, armure = ar.cuir_cloute,\
                     nom = "Neven", Lvl = 4, PO = 300, BBA = 1,mana=120, \
                      sorts=['boule de feu', ])

mitaine = cl.Personnage(13,13,13,13,\
                         PV=60,arme3=ar.arc_composite, arme2=ar.epee_courte_dex,\
                            arme1=ar.epee_courte_f,armure=ar.cuir_cloute,\
                         nom="Mitaine", Lvl=4, PO=337, BBA=2,\
                        dons=['tir_lointain'])
