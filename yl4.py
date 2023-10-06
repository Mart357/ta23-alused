#yl4
#Kirjuta programm, mis leiab kahest kasutaja poolt sisestatud arvust miinimumi (ära kasuta min funktsiooni). 
#(muutuja - variable, tingimus - condition, if-lause - if statement)
#1.küsi kasutajalt arv1
#2.küsi kasutajalt arv2
#leia miinimum väärtus
#väljasta see

a = input("sisesta a: ")
b = input("sisesta b: ")
if int(b) > int(a):
        print("miinimum on", a)
else:
        print("miinimum on", b)