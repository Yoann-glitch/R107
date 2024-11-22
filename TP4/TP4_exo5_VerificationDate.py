def est_bissextile(annee):
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

def verifier_date(date_str):
    if len(date_str) != 8 or not date_str.isdigit():
        print("Format de date invalide. Veuillez entrer une date sous la forme jjmmaaaa.")
        return

    jour = int(date_str[0:2])
    mois = int(date_str[2:4])
    annee = int(date_str[4:8])

    if mois < 1 or mois > 12:
        print("Mois invalide. Veuillez entrer un mois entre 01 et 12.")
        return


    if mois in [1, 3, 5, 7, 8, 10, 12]:
        if jour < 1 or jour > 31:
            print("Jour invalide. Ce mois a 31 jours.")
            return
    elif mois in [4, 6, 9, 11]:
        if jour < 1 or jour > 30:
            print("Jour invalide. Ce mois a 30 jours.")
            return
    elif mois == 2:
        if est_bissextile(annee):
            if jour < 1 or jour > 29:
                print("Jour invalide. Février a 29 jours cette année.")
                return
        else:
            if jour < 1 or jour > 28:
                print("Jour invalide. Février a 28 jours cette année.")
                return


    print("La date est valide.")

date_input = input("Entrez une date au format jjmmaaaa : ")
verifier_date(date_input)