txt = input("Sisesta suvaline tekst: ")
#txt = txt.replace(" ","").strip() # kui soovime, et eemaldaks ka keskelt
txt = txt.replace(" ","").strip()
length = len(txt)
center = int(length // 2)

if length : > = 7 and length % 2 == 1: #%2 paarituarvuline
    print("")
