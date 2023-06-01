"""Ejercicios"""


class Vehiculo:
    """Classe vehiculo"""

    def __init__(self, color: str, ruedas: int, puertas: int):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
        return f"Coche de color {self.color}, {self.puertas} puertas y {self.ruedas} ruedas."


class Coche(Vehiculo):
    """Classe coche"""

    def __init__(self, color: str, ruedas: int, puertas: int, velocidad: int, cilindrada: int):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + f" Con una velocidad de {self.velocidad} y {self.cilindrada} CV."


coche = Coche("Rojo", 4, 5, 120, 90)
print(coche)
