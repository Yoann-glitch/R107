import os.path
import datetime

def main():
    # Demande à l'utilisateur d'entrer les noms des fichiers
    fichier1 = input("Entrez le nom du premier fichier : ")
    fichier2 = input("Entrez le nom du deuxième fichier : ")

    # Vérifie si les fichiers existent
    if os.path.isfile(fichier1):
        taille1 = os.path.getsize(fichier1)
        print(f"Le fichier '{fichier1}' existe et sa taille est de {taille1} octets.")
        date_modif1 = os.path.getmtime(fichier1)
    else:
        print(f"Le fichier '{fichier1}' n'existe pas.")
        return

    if os.path.isfile(fichier2):
        taille2 = os.path.getsize(fichier2)
        print(f"Le fichier '{fichier2}' existe et sa taille est de {taille2} octets.")
        date_modif2 = os.path.getmtime(fichier2)
    else:
        print(f"Le fichier '{fichier2}' n'existe pas.")
        return

    # Compare les dates de modification
    if date_modif1 > date_modif2:
        date_modif1_formatee = datetime.datetime.fromtimestamp(date_modif1)
        print(f"Le fichier '{fichier1}' est le plus récent, modifié le {date_modif1_formatee}.")
    elif date_modif2 > date_modif1:
        date_modif2_formatee = datetime.datetime.fromtimestamp(date_modif2)
        print(f"Le fichier '{fichier2}' est le plus récent, modifié le {date_modif2_formatee}.")
    else:
        print("Les deux fichiers ont été modifiés à la même date.")

if __name__ == "__main__":
    main()