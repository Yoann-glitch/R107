def ajouter_elt(lst=[0, 1, 2], elt=3):
    print(f"ID de lst avant ajout : {id(lst)}")
    lst.append(elt)
    print(f"ID de lst après ajout : {id(lst)}")
    return lst

# a)
print("Résultat de ajouter_elt() :", ajouter_elt())

# b)
print("Résultat de ajouter_elt() :", ajouter_elt())

# c)
def ajouter_carac(ch="abc", elt="d"):
    return ch + elt

# d)
print("Résultat de ajouter_carac() :", ajouter_carac())

# e) Répéter l'instruction précédente
print("Résultat de ajouter_carac() :", ajouter_carac())