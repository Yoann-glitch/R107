# Demande à l'utilisateur de saisir un nombre X supérieur à 1
X = int(input("Veuillez saisir un nombre supérieur à 1 : "))

# Initialisation des variables
N = 0
somme = 0

# Boucle pour trouver le plus grand N tel que la somme soit <= X
while somme + N <= X:
    somme += N
    N += 1

# Affichage du résultat
# N a été incrémenté une fois de trop, donc on soustrait 1
print("Le plus grand nombre N tel que la somme de 0 à N est <= X est :", N - 1)