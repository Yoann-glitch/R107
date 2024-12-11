import random

# a) Fonction pour générer un tableau de 'nbr' valeurs comprises entre 'vmin' et 'vmax'
def generer(nbr, vmin, vmax):
    return [random.randint(vmin, vmax) for _ in range(nbr)]

# Fonction pour compter le nombre de valeurs d'un tableau 'table' inférieures à 'vseuil'
def combienInferieur(table, vseuil):
    return sum(1 for x in table if x < vseuil)

# Programme principal
def main():
    # Demande à l'utilisateur le nombre de valeurs à générer
    nb = int(input("Combien de nombres entiers voulez-vous générer ? "))

    # Demande à l'utilisateur l'intervalle
    vmin = int(input("Valeur minimale (vmin) : "))
    vmax = int(input("Valeur maximale (vmax) : "))

    # Génération des valeurs
    print(f"Générer {nb} nombres entiers entre {vmin} et {vmax}")
    tab = generer(nb, vmin, vmax)
    tab.sort()
    print("Tableau généré :", tab)

    # Demande à l'utilisateur s'il veut préciser le seuil
    reponse = input("Vous voulez préciser le seuil ? (Oui/O ou Non/N) : ").strip().lower()

    if reponse in ['oui', 'o']:
        seuil = int(input("Veuillez entrer le seuil : "))
    else:
        seuil = 30  # Valeur par défaut

    # Compte le nombre de valeurs inférieures au seuil
    total = combienInferieur(tab, seuil)
    print(f"Il y en a {total} inférieurs à {seuil}")

if __name__ == "__main__":
    main()