while True:

    x = int(input("Entre un nombre: "))

    if (x>0) and (x%2==0):
        print("Le nombre est positif et pair")
    elif (x<0) and (x%2==0):
        print("Le nombre est négatif et pair.")
    elif (x>0) and (x%2==1):
        print("Le nombre est positif est impair.")
    elif (x<0) and (x%2==1):
        print("Le nombre est negatif et impair.")
    else:
        print("Le nombre est 0.")