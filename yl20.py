# yl20
# Väljasta korduslause abil 8 korrutis arvudega 0..12 ja vorminda väljund nii:
# 8 x 0 = 0
# 	8 x 1 = 8
# 	8 x 2 = 16
# 	…
# 	8 x 12 = 96
# Täienda programmi nii, et kasutajalt küsitakse arv x, mille kohta korrutustabel väljastatakse


number = 8

for count in range (1 , 13):
    product = number * count
    print(number, "x", count, "=", product)

number = int(input("Sisesta number ühest kümneni: "))

for count in range (1 , 13):
    product = number * count
    print(number, "x", count, "=", product)