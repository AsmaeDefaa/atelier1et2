#définir une fonction pour compter les chiffres d'un nombre
def chiffres(n):
#fin de récursivité
   if n//10:
       return 1
   else:
#boucle de récursivité
         return 1+chiffres(n//10)
n=int(input("entre un nombre "))
#afficher le ruséltat de nombre des chiffres
print("le nobre des chifres",n,"est" ,chiffres(n))