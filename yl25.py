# Mõned asjad yl12-st
# Koosta dictonary

thisdict = {
    "first_name": "Märt",
    "last_name": "Pors",
    "birth_date": "1995",
    "location": "Kuressaare",
    "dessert": "Kohuke"
}

print(thisdict)

# Väljastamine kahel viisil
print(thisdict["location"])

x = thisdict.get("location")

print(x)

# Muudan väärtust
thisdict["birth_date"] = "1996"

print(thisdict)

# Väljastan võtmed 
for x in thisdict:
  print(x)

# Väljastan väärtused
for x in thisdict:
  print(thisdict[x])

# Kontrollin kas element on dictonarys 
print("Isikukood" in thisdict)

# leian elementide arvu
size = len(thisdict)
print(size)

# Lisan elemendi enda pikkuse jaoks
thisdict["Pikkus"] = "175"
print(thisdict)

# Eemaldan elemendi
thisdict.pop("birth_date")
print(thisdict)

# Kustutan dictonary
del thisdict
print(thisdict)