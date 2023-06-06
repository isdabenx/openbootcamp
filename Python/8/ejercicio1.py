"""En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y
escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado."""

FILE = "file.txt"

with open(FILE, 'w', encoding="UTF-8") as file:
    file.write("texto a escribir\n")

with open(FILE, 'a', encoding="UTF-8") as file:
    file.write("mas texto\n")

with open(FILE, 'r', encoding="UTF-8") as file:
    print(file.read())
