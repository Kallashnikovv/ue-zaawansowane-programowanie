def przetworz_listy(lista1, lista2):
    unikalne = set(lista1 + lista2)
    return [x**3 for x in unikalne]


l1 = [1, 2, 3]
l2 = [3, 4, 5]
print(przetworz_listy(l1, l2))
