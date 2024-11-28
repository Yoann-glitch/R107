nom1 = input("Entrez le nom de la première personne : ")
prenom1 = input("Entrez le prénom de la première personne : ")

nom2 = input("Entrez le nom de la deuxième personne : ")
prenom2 = input("Entrez le prénom de la deuxième personne : ")

personnes = [
    (nom1.lower(), prenom1.capitalize()),  # On met le nom en minuscules pour le tri
    (nom2.lower(), prenom2.capitalize())
]

personnes.sort()

for nom, prenom in personnes:
    print(f"{prenom} {nom.upper()}")