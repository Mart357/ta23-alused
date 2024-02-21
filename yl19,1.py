text = "ametikool"
vowels = "aeiouõäöü"

count = 0 

for c in text.lower():
    if c in vowels:
        count += 1 # count = count + 1

print(count)