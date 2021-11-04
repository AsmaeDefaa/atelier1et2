#définiton une sérrie Fibonnacci
def fib(n):
#boucle de récursivité
   if n<=1:
        return n
   else:
#boucle de récursivité
      return fib(n - 1) + fib(n - 2)
n=int(input("entre un nombre"))
#afficher le résultat
print(fib(n))