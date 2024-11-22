# MostFrequentWithCount.py

def element_le_plus_frequent(liste):
    element_max = liste[0]  # On suppose que la liste n'est pas vide
    max_occurrences = liste.count(element_max)

    for element in liste:
        occurrences = liste.count(element)
        if occurrences > max_occurrences:
            max_occurrences = occurrences
            element_max = element

    return element_max, max_occurrences

# Exemple de liste
liste = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7]

# Appel de la fonction
element, frequency = element_le_plus_frequent(liste)

# Affichage des résultats
print(f"Le nombre le plus frequent dans la liste est le : {element} ({frequency} x)")