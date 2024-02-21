b = " "

while not b.isnumeric():
    b = int(input("sisesta tegur: "))

b = int(b)

for a in range (0, 13):
    print(b, "x", a, "=", a * b)