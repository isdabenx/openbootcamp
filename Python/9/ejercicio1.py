"""Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben
almacenar en una lista. No debería haber países repetidos (haz uso de set). Finalmente, muestra por
consola la lista de países ordenados alfabéticamente y separados por comas."""

paises = input("Introduce una lista de paises separados por comas: ")
paises = paises.split(",")
paises = set(paises)
paises = list(map(lambda x: x.strip().capitalize(), paises))
paises.sort()
print(paises)
