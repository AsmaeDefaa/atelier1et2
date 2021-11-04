#definir une fonction factoriel
def factorielle(n):
    #fin de récursivité
    if n == 1:
        return n
    else:
# boucle de récursivité
     return n *factorial(n - 1)

# declaration de la boucle de la boucle pricipale
n = 0
x=int(input("donner votre nombre"))
#declaration de la boucle principale
for i in range(1, x + 1):
        n = (factorial(i)/i) + n
# afficher   le résultat final
print(n)