# a)
L1 = [0] * 3
print("Liste L1 :", L1)
print("Type de L1 :", type(L1))
print("ID de L1 :", id(L1))

# b)
for index, value in enumerate(L1):
    print(f"Élément à l'index {index} : valeur = {value}, type = {type(value)}, id = {id(value)}")

# c)
L1[1] += 1
print("\nListe L1 après modification :", L1)
print("Type de L1 après modification :", type(L1))
print("ID de L1 après modification :", id(L1))

# d)
for index, value in enumerate(L1):
    print(f"Élément à l'index {index} : valeur = {value}, type = {type(value)}, id = {id(value)}")

# e)
ma_chaine = "machaine"
print("\nChaîne :", ma_chaine)
print("ID de ma_chaine :", id(ma_chaine))
print("Type de ma_chaine :", type(ma_chaine))

# Affichage de l'identifiant de chaque caractère de la chaîne
for index, char in enumerate(ma_chaine):
    print(f"Caractère à l'index {index} : '{char}', type = {type(char)}, id = {id(char)}")