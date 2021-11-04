#creer une liste l1 et l2 avec des donnees
l1=[9,5,7,3,16]
l2=[7,9,2]
l=[]
count=0
for i in l1:
    if count%2 !=0:
        l.append(i)#ajouter les elements d'indices impaire dans la listel
    count +=1

for j in l2:
    if count%2==0:
        l.append(j)#ajouter les elements d'indices pair dans la liste l
    count +=1
    #affiche le resultat
print(l)
