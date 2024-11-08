import time

x = int(input("Enter la valeur : "))
y = x

print("\nFor :")
for i in range (x):
    print(x)
    x -= 1
    time.sleep(0.5)

print("\nWhile :")
while y > 0:
    print(y)
    y -= 1
    time.sleep(0.5)