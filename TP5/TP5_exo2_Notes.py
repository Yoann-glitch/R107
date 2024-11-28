notes = []
coefficients = []

for i in range(5):
    valeurs = input(f"Veuillez entrer la note du module {i+1} et le coefficient correspondant : ")
    note, coefficient = valeurs.split()
    notes.append(float(note))
    coefficients.append(int(coefficient))

moyenne_generale = sum(note * coefficient for note, coefficient in zip(notes, coefficients)) / sum(coefficients)

if moyenne_generale > 10 and all(note >= 8 for note in notes):
    print("L'étudiant est admis.")
else:
    print("L'étudiant n'est pas admis.")

print(f"Moyenne générale : {moyenne_generale:.2f}")