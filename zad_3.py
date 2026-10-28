def czy_parzysta(liczba):
    return liczba % 2 == 0


wynik_parzystosci = czy_parzysta(8)

if wynik_parzystosci:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
