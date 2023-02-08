from math import *
num12 = "1", "2"
cipher = (input("Kryptosträng? : "))
lencipher = len(cipher)
hurmanga1 = cipher.count(num12[0]) + 1
hurmanga2 = cipher.count(num12[1])
hurmanga = hurmanga2 + hurmanga1

for i in cipher.split():
    if i == 1 or 2:
        if int(i) + 1 == 7 or 8 or 9 and i == 2:
            hurmanga -= 1
        if int(i) + 2 == 0:
            hurmanga -= 1
        if int(i[-1]) == 1 or 2:
            hurmanga -= 1
        if int(i) + 1 == 1 or 2:
            hurmanga += 1
print(factorial(hurmanga))
