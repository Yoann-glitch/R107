import os
import sys

def aide():
    """Affiche un message d'aide sur l'utilisation du script."""
    print("Usage : python find1.py <chemin_du_dossier>")
    print("Veuillez fournir un chemin valide vers un dossier.")

def affiche(dossier):
    """Affiche le contenu du dossier passé en argument."""
    try:
        # Liste les fichiers et dossiers dans le dossier
        contenu = os.listdir(dossier)
        print(f"Contenu du dossier '{dossier}' :")
        for item in contenu:
            print(item)
    except Exception as e:
        print(f"Erreur lors de l'accès au dossier : {e}")

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

    # Appeler la fonction affiche pour afficher le contenu du dossier
    affiche(chemin_dossier)

if __name__ == "__main__":
    main()