import random

number = random.randint(1,100)
guess = 0

while guess != number:

    guess = int(input("Sisesta number ühest sajani: "))

    if (guess < number):
        print("Paku suuremat arvu!: ")
    elif (guess > number):
        print(" Paku väiksemat arvu!: ")   
    else:
        print("Sa võitsid!")