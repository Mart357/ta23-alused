# yl21
# Arvu arvamise mäng. 
# Arvuti mõtleb välja arvu nullist sajani. Lase kasutajal pakkuda, mis arvu arvuti välja mõtles. Vale pakkumise korral annab arvuti vihje, kas pakkumine on õigest arvust suurem või väiksem. Pakkuda saab seni, kuni kasutaja on õige arvu pakkunud. (juhuarv - random)
# # 

import random

secret = random.randrange(1, 101)
guess = 0

print(secret)

while secret != guess:
    guess = int(input("paku arv 1..100: "))

    if guess < secret:
        print("paku suurem")
    
    elif guess < secret:
        print("paku v2iksem arv")

    else:
        print("sa v6itsid!")