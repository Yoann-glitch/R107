nombre = float(input("Vous cherchez la table de multiplication de quel nombre ? "))

table_multiplication = []

for i in range(10):
    resultat = nombre * i
    table_multiplication.append(round(resultat, 1))#round permet de réduire le nombre de chiffre après la virgule

for i in range(10):
    print(f"{nombre} * {i} = {table_multiplication[i]}")