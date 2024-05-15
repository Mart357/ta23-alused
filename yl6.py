#yl6
#Kirjuta programm, mis leiab kolmest kasutaja poolt sisestatud arvust maksimumi (ära kasuta max funktsiooni). (loogikatehted - logic operators)

#leia kasutaja 1 arv
#leia kasutaja 2 arv
#leia kasutaja 3 arv
#leia maksimum arv
#väljastamine

a = int(input("Sisesta arv a: "))
b = int(input("Sisesta arv b: "))
c = int(input("Sisesta arv c: "))

if a > b and a > c:  #võrdlutehted
    print("maksimum on", a)

elif b > c:
    print("maksimum on", b)
    
else:
    print("maksimum on", c)