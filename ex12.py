# ecrire une fonction pour conventir le nombre décimal en nombre binaire
def binaire (nbr):
    result = ""
    if num >= 1:
        result = result + str(nbr % 2)
        return result + binaire(nbr // 2)

    return result
#écrire une fonction pour inverser le string pour trouver le nombre binaire
def reverse(string):
    return string[::-1]

#écrire une fonction pricipale
def main(nbr):
    return (inverser(binaire(nbr)))
print(main(int(input("entrer un nombre:\n"))))