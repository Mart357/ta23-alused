# yl21
# Arvu arvamise mäng. 
# Arvuti mõtleb välja arvu nullist sajani. Lase kasutajal pakkuda, mis arvu arvuti välja mõtles. Vale pakkumise korral annab arvuti vihje, kas pakkumine on õigest arvust suurem või väiksem. Pakkuda saab seni, kuni kasutaja on õige arvu pakkunud. (juhuarv - random)


import random

number = random.randint(0,100)
guess = 0

while guess != number:

    guess = int(input("Sisesta number ühest sajani: "))

    if (guess < number):
        print("Paku suuremat arvu!: ")
    elif (guess > number):
        print(" Paku väiksemat arvu!: ")   
    else:
        print("Sa võitsid!")