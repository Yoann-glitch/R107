# Demande l'âge de l'utilisateur
age = int(input("Veuillez entrer votre âge : "))

# Calcule l'année de naissance
from datetime import datetime

# Récupère l'année actuelle
annee_actuelle = datetime.now().year

# Calcule l'année de naissance
annee_naissance = annee_actuelle - age

# Affiche l'année de naissance
print(f"Votre année de naissance {annee_naissance}.")