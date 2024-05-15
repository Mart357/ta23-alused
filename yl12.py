# Tekitan listi 
mylist = ["banaan", "õun", "pirn"]
print(mylist)

# Prindin listi esimese elemendi
print(mylist[0])

# Lisan listi elemendi
mylist.append("apelsin")
print(mylist)

# Prindin listi viimase elemendi
print("viimane", mylist[-1])

# Muuda ühe elemendi väärtust ja väljasta kogu list
mylist[2] = "ploom" # muudab listis oleva 3.positsioonil oleva elemendi ploomiks
print(mylist)

# Leian kas listis on element
check = input("kontrolli listis puuvilja: ")

if check in mylist:
    print(check, "on listis")
else:
    print(check, "ei ole listis")

# leian elementide arvu
size = len(mylist)
print(size)

# Eemaldan elemendi
mylist.remove("banaan")
print(mylist)

# Keeran elemendide listi teist pidi
mylist.reverse()
print(mylist)

# Sorteerin listi(tähestiku järjekorras)
# mylist.sort()
print(sorted(mylist))
print(mylist)

