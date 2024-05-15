#Kirjuta programm, mis küsib kasutajalt sisendina stringi.
word = input("Kirjuta oma lemmikriik: ")
#Eemalda selle sisendi algusest ja lõpust tühikud.
word = word.strip() #esimesed jutumärgid võtavad ära tühikud ja teine jutumärk asendab.
print(word)
#String peab vastama tingimustele, et selles on vähemalt seitse sümbolit ja et sümbolite arv on paaritusarvuline.
length = len(word)
if length >= 7 and length % 2 == 1:    # >=  kas v2iksem v6i kaasaarvatud sama v22rtuseline
    print(length // 2)
    middle = length // 2
    print(word[middle-1: middle+2])
#Väljasta selle stringi kolm keskmist sümbolit.
    
else:
    print("ei vasta tingimustele")
#(stringi meetodid, list)