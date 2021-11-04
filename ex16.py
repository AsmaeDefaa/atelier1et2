#définir une fonction tri par insertion
#en mutant chaque valeur du tableau selon si elle est supérieure à sa va-leur précédente / suivante
def tri_par_insertion(l1):
    i =  0
    while( i < len(l1) - 1):
        if l1[i] > l1[i + 1]:
            j = l1[i + 1]
            l1[i + 1] = l1[i]
            l1[i] = j
        i = i + 1
    return l1
#définir une fonction tri a bull
#en itérant toute la liste et en obtenant le minimum à chaque fois et en l'ajoutant à une nouvelle liste
def tri_a_bull(l1, a):
    if l1== []:
        return a
    num1 = min(l1)
    a.append(num1)
    l1.remove(num1)
    return tri_a_bull (l1, list(a))

#définir une fonction tri par sélection
#en choisissant un élément et en le comparant au reste de la liste et en mutant si nous avons trouvé plus grand que ce dernier
def tri_par_selection(l1):
    n = len(l1)
    for i in range(0, n - 2):
        min = i
        for j in range(i + 1, n - 1):
            if l1[j] < l1[min]:
                min = j
        if min != i:
            temp = l1[min]
            l1[min] = l1[i]
            l1[i] = temp
    return l1


#affichage finale
print(tri_par_insertion([1, 22, 3, 9, 8]))
print(tri_par_selection([1, 9, 7, 6, 2]))
print(tri_a_bull([9, 5, 17, 2, 18], []))
