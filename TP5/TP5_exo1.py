# nomprenom.py

# Entrée des informations pour la première personne
nom1 = input("Entrez le nom de la première personne : ")
prenom1 = input("Entrez le prénom de la première personne : ")

# Entrée des informations pour la deuxième personne
nom2 = input("Entrez le nom de la deuxième personne : ")
prenom2 = input("Entrez le prénom de la deuxième personne : ")

# Création d'une liste de tuples pour stocker les noms et prénoms
personnes = [
    (nom1.lower(), prenom1.capitalize()),  # On met le nom en minuscules pour le tri
    (nom2.lower(), prenom2.capitalize())
]

# Tri de la liste par nom puis par prénom
personnes.sort()

# Affichage des résultats
for nom, prenom in personnes:
    print(f"{prenom} {nom.upper()}")