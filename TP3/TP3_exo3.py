import random

rNumber = random.randint(0,99)
guess = int(input("Devine le nombre : "))
count = 1

while guess != rNumber:
    if rNumber > guess:
        print("Le nombre est + grand !")
    elif rNumber < guess:
        print("Le nombre est + petit !")
    count += 1
    guess = int(input("\nTry to guess the number :"))

print("\nTu as deviner le nombre!")
print("Le nombre était",rNumber,".")
print("Tu l'as trouvé en ",count,"essais.")