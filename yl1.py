# yl1
# Kirjuta programm, mis teisendab kasutaja poolt kroonides sisestatud summa eurodesse
# ja väljastab ümardatud tulemuse. (round)

#//float funktsioon lubab teha arvu komaarvuks.
#round on ümardamise funktsioon, kus määrad ära mitu kohta peale komaga arvu sa tulemuse väljastad.

eek = float (input("Sisesta kroonid: "))
eur = round(eek / 15.6466, 3)
print(eur)