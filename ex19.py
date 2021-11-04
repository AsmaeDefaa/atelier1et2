#définir une fonction pour chercher un élément dans une matrice puis renvoi sa position <<i,j>>
def cherche(l):
    for i in l:
        a=0
        for j in i :
            if j==n:
               print("i=",l.index(i),"j=",a)
            a=a+1
#créer une matrice avec des données
l=[[8,9,4],
       [5,3,1],
       [1,16,4]]
n=int(input("saisir la valeur chercher"))
#aficher le résultat final
print(cherche(l))
