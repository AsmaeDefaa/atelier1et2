# définition d'une fonction som
def som(n):
#fin de récursivité
    if n == 1:
        return 1
    else:
#boucle de récursivité
        return (n + som(n-1))
n=int(input("donner une valeur :"))
# aficher le résultat
print(sum(int(input("get here the n \n"))))