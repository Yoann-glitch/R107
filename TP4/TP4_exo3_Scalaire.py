nMax = 3

v1 = []
v2 = []

n = int(input(f"Quelle est la taille de vos vecteurs [entre 1 et {nMax}] ? "))

while n < 1 or n > nMax:
    n = int(input(f"Veuillez entrer une valeur valide entre 1 et {nMax} : "))

print("Saisie du premier vecteur :")
for i in range(n):
    val = int(input(f"v1[{i}] = "))
    v1.append(val)

print("Saisie du second vecteur :")
for i in range(n):
    val = int(input(f"v2[{i}] = "))
    v2.append(val)

produit_scalaire = sum(v1[i] * v2[i] for i in range(n))

print(f"Le produit scalaire de v1 par v2 vaut {produit_scalaire}.")