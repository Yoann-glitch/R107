def element_le_plus_frequent(liste):
    occurrences = {}

    for element in liste:
        if element in occurrences:
            occurrences[element] += 1
        else:
            occurrences[element] = 1

    element_max = None
    max_occurrences = 0

    for element in liste:
        if occurrences[element] > max_occurrences:
            max_occurrences = occurrences[element]
            element_max = element

    return element_max, max_occurrences

liste = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7]

element, frequency = element_le_plus_frequent(liste)

print(f"Le nombre le plus frequent dans la liste est le : {element} ({frequency} x)")