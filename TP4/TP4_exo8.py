# tp4exo8.py

# Création des dictionnaires pour chaque étudiant
etudiant1 = {
    "name": "MULLER",
    "firstname": "Yoann",
    "promo": 2024,
    "group": 13
}

etudiant2 = {
    "name": "Hartmann",
    "firstname": "Quentin",
    "promo": 2024,
    "group": 13
}

print("Les clés du dictionnaire sont :")
for key in etudiant1.keys():
    print(f"- {key}")

print("Les valeurs du dictionnaire sont :")
for value in etudiant1.values():
    print(f"- {value}")

print("Les tuplets du dictionnaire sont :")
for item in etudiant1.items():
    print(f"- {item}")

binome = {
    "etudiant1_id": etudiant1,
    "etudiant2_id": etudiant2
}

print("Les étudiants formants le binôme sont :")
print(f"- L'étudiant {etudiant1['name']} {etudiant1['firstname']} du groupe {etudiant1['group']}")
print(f"- L'étudiant {etudiant2['name']} {etudiant2['firstname']} du groupe {etudiant2['group']}")