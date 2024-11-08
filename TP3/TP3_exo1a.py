def somme_entiers(N):
    return N * (N + 1) // 2

N = int(input("Entrez un entier naturel N : "))
resultat = somme_entiers(N)
print("La somme des entiers de 0 à", N, "est :", resultat)