#définir une fonction pour trouver la fréquence d’un caractère dans une chaîne
def count(c):
 count=0
 for i in text:# écrire une boucle for pour parcourir les éléments du text
  if i==c:
    count += 1
text = (input("entrer un texte:"))
c = (input("entrer le  caractére:"))

count =text.count
#appeler la fonction et aficher le résultat final
print( count(c))
