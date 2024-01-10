text = input("Sisesta tekst: ")
count = 0
for character in text:
    if character.lower() in "aeiouõäöü":
        count += 1

print("count:", count)