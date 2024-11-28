def selection_sort(tab):
    n = len(tab)
    for i in range(n - 1):

        min_idx = i

        for j in range(i + 1, n):
            if tab[j] < tab[min_idx]:
                min_idx = j

        tab[i], tab[min_idx] = tab[min_idx], tab[i]
        print(tab)


def print_array(tab):
    for val in tab:
        print(val, end=" ")
    print()

tab = [89, 19, 56, 381, 90]

print(f"Selection Sort :\nListe de base: ", end="")
print_array(tab)
print("Commencement du tri")
selection_sort(tab)
print("-= Finish Sorting =-")
print("Fin du tri: ", end="")
print_array(tab)

tab = [89, 19, 56, 381, 90]
print(f"\ntab.sort() :\nListe de base: {tab}")
tab.sort()
print(f"Liste à la fin: {tab}")

tab = [89, 19, 56, 381, 90]
print(f"\nsorted(tab) :\nListe de base: {tab}\nFinn de la liste: {sorted(tab)}")