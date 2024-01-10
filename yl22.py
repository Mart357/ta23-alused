import random

options = ("kivi", "paber", "käärid")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Sisesta valik: (kivi, paber, käärid): ")

    print(f"Mängija: {player}")
    print(f"Arvuti: {computer}")

    if player == computer:
        print("Viik!")
    elif player == "kivi" and computer == "käärid":
        print("Sina võitsid!")
    elif player == "paber" and computer == "kivi":
        print("Sina võitsid!")
    elif player == "käärid" and computer == "paber":
        print("Sina võitsid!")
    else:
        print("Sina kaotasid!")

    if not input("Soovid veel mängida? (y/n): ").lower() == "y":
        running = False

print("Aitäh mängimast!")
