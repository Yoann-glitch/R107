heures_travaillees = float(input("Veuillez entrer le nombre d'heures travaillées : "))
salaire_horaire = float(input("Veuillez entrer le salaire horaire : "))

if heures_travaillees <= 160:
    salaire = heures_travaillees * salaire_horaire
elif heures_travaillees <= 200:
    salaire = (160 * salaire_horaire) + ((heures_travaillees - 160) * salaire_horaire * 1.25)
else:
    salaire = (160 * salaire_horaire) + (40 * salaire_horaire * 1.25) + ((heures_travaillees - 200) * salaire_horaire * 1.5)

print(f"Le salaire total pour {heures_travaillees} heures travaillées est de : {salaire:.2f} euros.")