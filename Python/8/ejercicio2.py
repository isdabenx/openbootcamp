"""En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo,
haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos."""

import pickle

class Vehiculo:
    """Classe vehiculo"""

    def __init__(self, color: str, ruedas: int, puertas: int):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
        return f"Coche de color {self.color}, {self.puertas} puertas y {self.ruedas} ruedas."
    

v1 = Vehiculo("rojo", 4, 5)

with open("vehiculo.dat", "wb") as file:
    pickle.dump(v1, file)

with open("vehiculo.dat", "rb") as file:
    v2 = pickle.load(file)

print(v2)
