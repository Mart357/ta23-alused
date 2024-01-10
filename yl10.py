#Kirjuta programm, mis küsib kasutajalt nime, tervitab teda nimepidi, küsib kasutajalt elukoha, kui elukoht on Saaremaa, siis väljastab mingi kommentaari.
#küsib kasutajalt vanuse, kui vanus on väiksem kui 18, siis ütleb, et kasutaja on liiga noor, et autot juhtida.
# kui vanus on 18, siis õnnitleb täisealiseks saamise puhul, kui kasutaja on vanem kui 18, siis ütleb, et kasutaja võib autot juhtida. (sõne - string)


print("Tere, mis on Sinu nimi?") 
name = input("nimi:")

print("Tere,", name + "!")
location = input("Kust sa pärit oled? ").lower()

if location == ("Saaremaa") or location == ("saaremaa"):
   print("tere saarlane!")
age = int(input("Kui vana Te olete? "))

if age==18:
  print("Õnnitlen Teid täisealiseks saamise puhul!")

elif age<18:
    print("Olete liiga noor, et autoga sõita") 
    
else:
  print("Olete piisavalt vana, et autot juhtida.")