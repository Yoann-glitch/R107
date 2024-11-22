nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moy = 0.0

notes = []

somme_notes = 0.0
for i in range(nombreEtudiants):
    while True:
        note = float(input(f"Note etudiant {i} : "))
        if 0 <= note <= 20:
            notes.append(note)
            somme_notes += note
            break
        else:
            print("Veuillez saisir une note valide entre 0 et 20.")

moy = somme_notes / nombreEtudiants if nombreEtudiants > 0 else 0

print(f"Moyenne de classe : {moy:.2f}")
print("Numéro de l’Etudiant | note | ecart a la moyenne")
for i in range(nombreEtudiants):
    ecart = notes[i] - moy
    print(f"{i} | {notes[i]:.1f} | {ecart:.2f}")