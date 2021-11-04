list1 =[47,64,69,37,76,83,95,97]
dict1={'yassine':47,'imane':69,'Mohamed':76,'abir':97}
keys= list(dict1.keys())
result=[]
for i in keys:
    for j in list1:#boucle pour parcourir la liste
        if dict1[str(i)]==j:result.append(j)#ajouter les elements j au dict1
print(result)#affiche le resultat final
