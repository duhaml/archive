def calcul_somme(liste):
    # calcule la somme d argent a partir d une liste de noms de pieces
    somme = 0
    for i in liste :
        valeur = CatalogueValeurs[i]
        somme+=valeur
    return round(somme,2)

CatalogueValeurs={'2e':2,'1e':1,'50c':0.5,'20c':0.2,'10c':0.1,'5c':0.05,'2c':0.02,'1c':0.01,'Xc':0.02,'X0c':0.2}
#le catalogue CatalogueValeurs est sous la forme {nom:valeur}


def catalogue(liste):
    # retourne un dictionnaire contenant les valeurs de pieces rencontrees et les occurrences correspondantes
    cata={} #le catalogue cata est créé avec les composants de liste, de la forme {nom:nombre_d_occurences}
    for x in liste :
        nom = x
        if nom in cata:
            cata[x]+=1
        else:
            cata[x]=1
    return cata


