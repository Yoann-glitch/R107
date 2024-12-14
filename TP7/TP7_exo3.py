import os
import sys

def recherche(dossier):
    """Recherche les fichiers et dossiers dans le dossier donné."""
    listeFichiers = []
    listeDossiers = []

    # Parcourir le contenu du dossier
    try:
        for element in os.listdir(dossier):
            chemin_complet = os.path.join(dossier, element)  # Chemin complet de l'élément

            if os.path.isdir(chemin_complet):
                listeDossiers.append(chemin_complet)  # Ajouter à la liste des dossiers
            elif os.path.isfile(chemin_complet):
                listeFichiers.append(chemin_complet)  # Ajouter à la liste des fichiers

    except Exception as e:
        print(f"Erreur lors de l'accès au dossier : {e}")
        return listeFichiers, listeDossiers

    # Boucle pour explorer les sous-dossiers
    for sous_dossier in listeDossiers:
        fichiers_sous_dossier, dossiers_sous_dossier = recherche(sous_dossier)  # Appel récursif
        listeFichiers.extend(fichiers_sous_dossier)  # Ajouter les fichiers trouvés
        listeDossiers.extend(dossiers_sous_dossier)  # Ajouter les sous-dossiers trouvés

    return listeFichiers, listeDossiers

def aide():
    """Affiche un message d'aide sur l'utilisation du script."""
    print("Usage : python find2.py <chemin_du_dossier>")
    print("Veuillez fournir un chemin valide vers un dossier.")

def main():
    # Vérifier le nombre d'arguments
    if len(sys.argv) != 2:
        print("Erreur : Nombre d'arguments incorrect.")
        aide()
        return

    chemin_dossier = sys.argv[1]

    # Vérifier si le chemin est un dossier existant
    if not os.path.exists(chemin_dossier):
        print(f"Erreur : Le dossier '{chemin_dossier}' n'existe pas.")
        aide()
        return
    if not os.path.isdir(chemin_dossier):
        print(f"Erreur : '{chemin_dossier}' n'est pas un dossier.")
        aide()
        return

    # Appeler la fonction recherche pour obtenir les fichiers et dossiers
    listeFichiers, listeDossiers = recherche(chemin_dossier)

    # Afficher les résultats
    print("Liste des fichiers :")
    for fichier in listeFichiers:
        print(fichier)

    print("\nListe des dossiers :")
    for dossier in listeDossiers:
        print(dossier)

if __name__ == "__main__":
    main()