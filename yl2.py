# yl2
# Kirjuta programm, mis küsib kasutajalt raadiuse ja arvutab ringi pindala ja ümbermõõdu. (math.pi)
# küsime kasutajalt raadiuse
# arvutame ringi pindala
# arvutame ringi raadiuse
# väljastame c, s

from math import pi 

radius = float(input("Sisesta raadius:"))
area = pi * radius ** 2
print("Pindala:", area)

perimeter = 2 * pi * radius
print("Ümbermõõt:", perimeter)
