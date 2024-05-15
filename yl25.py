# Koosta dictionary vähemalt viie endale iseloomuliku tunnusega (näiteks: eesnimi, perenimi, sünniaasta, elukoht, lemmik magustoit).
#Väljasta elukoht kahel erineval viisil (kasutades get() meetodit ja mitte kasutades seda).
#Muuda magustoidu väärtust.
#Tee kordus üle dictionary ja väljasta kõik võtmed.
#Tee kordus üle dictionary ja väljasta kõik väärtused (pööra tähelepanu sellele, et saab mitmel viisil, proovi erinevaid võimalusi).
#Kontrolli, kas isikukood on dictionary's olemas.
#Leia dictionary suurus (elementide arv).
#Lisa element enda pikkuse jaoks.
#Eemalda element sünniaasta (pane tähele, et saab mitut moodi).
#Pane tähele, et del võtmesõnaga on võimalik kogu dictionary kustutada.
#Saa aru ja katseta del võtmesõna ja clear meetodi erinevusest.
#Tutvu kõigi dictionary meetoditega.
#Läbi ülesanne juhendi lõpus.
#https://www.w3schools.com/python/python_dictionaries.asp


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