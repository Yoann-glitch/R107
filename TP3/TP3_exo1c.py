valeurs = []
for _ in range(10):
    while True:
        valeur = float(input("Entrez une valeur entre 0 et 20 : "))
        if 0 <= valeur < 20:
            valeurs.append(valeur)
            break
        else:
            print("Valeur invalide. Veuillez réessayer.")

# Compter les valeurs dans chaque intervalle
moins_de_10 = sum(1 for v in valeurs if v < 10)
entre_10_et_15 = sum(1 for v in valeurs if 10 <= v < 15)
plus_de_15 = sum(1 for v in valeurs if v >= 15)

print("Nombre de valeurs inférieures à 10 :", moins_de_10)
print("Nombre de valeurs entre 10 et 15 :", entre_10_et_15)
print("Nombre de valeurs supérieures ou égales à 15 :", plus_de_15)
