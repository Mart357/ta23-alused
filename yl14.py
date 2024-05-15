filename = input('Sisesta failinimi .ext kujul: ')

ext = filename.split('.')
print(ext)
print("Faili laiend on : ", ext[-1] if len(ext) > 1 else "Tundmatu laiendus")