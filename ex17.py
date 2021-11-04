#définition d'une fonction pour inverser les lettres d'une chaine de caractéres
def inverse(a):
    inv=" "
    for i in range(len(a)):#écrire une boucle for pourparcourir la liste a
        inv=inv+a[::-1]#[start:end:steps]<- on utilise le pas négative pour inverser
        return inv
a=input("entre un mot:")
#appler la fonction inverse (a)
print("l'inverse du mot",a,"est",inverse(a))
