# Zadanie 2a
def greet(names):
    for name in names:
        print(f"{name}")


names = ["Igor", "Gabriel", "Jakub", "Karolina", "Michał"]
greet(names)


# Zadanie 2b
def zad2bi(liczby):
    wynik = []
    for liczba in liczby:
        wynik.append(liczba * 2)
    return wynik


dane = [3, 7, 1.5, 10, -4]
print(zad2bi(dane))


def zad2bii(liczby):
    return [liczba * 2 for liczba in liczby]


dane = [3, 7, 1.5, 10, -4]
print(zad2bii(dane))


# Zadanie 2c
def wyswietl_parzyste(liczby):
    for i in range(len(liczby)):
        if liczby[i] % 2 == 0:
            print(liczby[i])


dane = list(range(1, 11))

print("Elementy parzyste:")
wyswietl_parzyste(dane)


# Zadanie 2d
def wyswietl_co_drugi(liczby):
    for i in range(0, len(liczby), 2):
        print(liczby[i])


dane = list(range(10, 110, 10))

print("Co drugi element:")
wyswietl_co_drugi(dane)
