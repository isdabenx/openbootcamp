"""En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno
que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar
sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o
no."""


class Alumno:
    """Alumno"""
    def __init__(self, nombre: str = None, nota: float = None) -> None:
        self.nombre = nombre
        self.nota = nota

    def set_nombre(self, nombre: str) -> None:
        """Set nombre"""
        self.nombre = nombre

    def get_nombre(self) -> str:
        """Get nombre"""
        return self.nombre

    def set_nota(self, nota: float) -> None:
        """Set nota"""
        self.nota = nota

    def get_nota(self) -> float:
        """Get nota"""
        return self.nota

    def resumen(self) -> None:
        """Imprime un resumen"""
        if not self.nombre or not self.nota:
            print("No hay datos del alumno, recuerda en poner el nombre y la nota.")
        else:
            print(f"Alumno: {self.nombre}")
            print(
                f"Ha {'aprobado' if self.nota >= 5 else 'suspendido'} con una nota de {self.nota}"
                )


pepito = Alumno()
pepito.set_nombre("Pepito")
pepito.set_nota(4.7)

maria = Alumno("Maria", 5.1)

juan = Alumno("Juan")
juan.set_nota(7.4)

fernando = Alumno()

pepito.resumen()
print()
maria.resumen()
print()
juan.resumen()
print()
fernando.resumen()
