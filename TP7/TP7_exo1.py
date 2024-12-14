import sys

def main():
    # Récupérer le nom du script et les arguments
    nom_du_script = sys.argv[0]
    arguments = sys.argv[1:]  # Les arguments commencent à l'index 1

    # Vérifier le nombre d'arguments
    nombre_d_arguments = len(arguments)

    if nombre_d_arguments == 0:
        print(f"Pas assez d’arguments pour le script '{nom_du_script}'")
    else:
        print(f"Nombre d'arguments : {nombre_d_arguments}")
        print("Arguments fournis :")
        for arg in arguments:
            print(arg)

if __name__ == "__main__":
    main()