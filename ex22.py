#creer une liste l avec des donnes
l=[1,5,77,54,18,17,16,33,1]
a=len(l)//3 #diviser la liste en tois morceaux
b=2*len(l)//3
l1=l[:a]
l2=l[a:b]
l3=l[b:]
#inverser les 3 morceaux puis l'afficher
print(l1[::-1],l2[::-1],l3[::-1])