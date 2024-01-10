string = input("Sisesta string, mis sisaldab vähemalt 7 sümbolit ja on paarituarvuline: ")

x = len(string)

y = x//2

print("Stringi kolm keskmist elemnti on:" ,string[y-1]+string[y]+string[y+1])