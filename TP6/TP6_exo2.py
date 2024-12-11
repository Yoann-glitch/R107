def ajouter_elt(lst, elt):
    lst.append(elt)
    return lst

# a) Première liste
lst1 = [0, 1, 2]

# b) 2ème liste
lst2 = ajouter_elt(lst1.copy(), len(lst1))  # On utilise lst1.copy() pour ne pas modifier lst1

# c) Affichage contenu, type et identifiant de chaque liste
for i, lst in enumerate([lst1, lst2], start=1):
    print(f"Liste lst{i} : {lst}")
    print(f"Type de lst{i} : {type(lst)}")
    print(f"ID de lst{i} : {id(lst)}\n")