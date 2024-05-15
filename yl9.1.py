def kolmnurga_liik(a, b, c):   # siind defineeritakse funktsioon
    if a + b <= c or a + c <= b or b + c <= a:  #<= Kui mõni külgede pikkuste paaride summa on väiksem või võrdne kolmanda külje pikkusega, siis kolmnurka ei eksisteeri.
        return "Sellise külgedega kolmnurka ei eksisteeri"
    elif a == b == c:
        return "Võrdkülgne kolmnurk"
    elif a == b or a == c or b == c:
        return "Võrdhaarne kolmnurk"
    else:
        return "Erikülgne kolmnurk"
def main():
    try:
        a = float(input("Sisestage esimese külje pikkus: "))
        b = float(input("Sisestage teise külje pikkus: "))
        c = float(input("Sisestage kolmanda külje pikkus: "))
        vastus = kolmnurga_liik(a, b, c)
        print(vastus)
    except ValueError:
        print("Palun sisestage arvulised väärtused külgede pikkusteks.")
if __name__ == "__main__":
    main()