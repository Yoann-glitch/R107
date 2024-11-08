x = input("Entrez x:" )
y = input("Entrez y:")
z = 0

x= int(x)
y= int(y)


print("Avant permutation")
print("x:",x)
print("y:",y)

z = x
x = y
y = z


print("Après permutation")
print("x:",x)
print("y:",y)