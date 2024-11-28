# 1. Calculer la taille de la chaîne de caractères T
def taille_chaine(T):
    taille = 0
    for char in T:
        if char == '\0':  # Caractère de fin de chaîne
            break
        taille += 1
    return taille


# 2. Calculer le pourcentage de voyelles dans la chaîne de caractères
def pourcentage_voyelles(T):
    taille = taille_chaine(T)
    voyelles = 0
    for char in T:
        if char in 'aeiouAEIOU':
            voyelles += 1
        if char == '\0':  # Caractère de fin de chaîne
            break
    if taille > 0:
        pourcentage = (voyelles / taille) * 100
    else:
        pourcentage = 0
    return pourcentage


# 3. Tester si la chaîne "wagon" est une sous-chaîne de T
def sous_chaine(T, sous_chaine):
    taille_T = taille_chaine(T)
    taille_sous_chaine = len(sous_chaine)

    for i in range(taille_T - taille_sous_chaine + 1):
        if T[i:i + taille_sous_chaine] == sous_chaine:
            return i
    return -1  #


# 4. Calculer le nombre d’occurrences de la chaîne "wagon" dans T
def compter_occurrences(T, sous_chaine):
    occurrences = 0
    taille_T = taille_chaine(T)
    taille_sous_chaine = len(sous_chaine)

    for i in range(taille_T - taille_sous_chaine + 1):
        if T[i:i + taille_sous_chaine] == sous_chaine:
            occurrences += 1
    return occurrences

T = "bonjour wagon, c'est un wagon dans le train.\0"  # Exemple de chaîne avec un caractère de fin

print("Taille de la chaîne :", taille_chaine(T))

print("Pourcentage de voyelles :", pourcentage_voyelles(T), "%")

index = sous_chaine(T, "wagon")
if index != -1:
    print('"wagon" est une sous-chaîne de T, début à l\'index :', index)
else:
    print('"wagon" n\'est pas une sous-chaîne de T.')

occurrences = compter_occurrences(T, "wagon")
print('Nombre d\'occurrences de "wagon" dans T :', occurrences)