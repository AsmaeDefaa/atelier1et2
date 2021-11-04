#creer une liste l avec des donnes
list1=[7,9,16,16,17]
d={}#donner un dictionnaire vide
for i in list1:#ecrire une boucle pour parcourir la list1
    if str(i) in d:
        d[str(i)]=d.get(str(i))+1
    else :
        d[str(i)]=1
#afficher le resultat
print(d)