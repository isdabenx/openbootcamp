"""En este ejercicio tendréis que crear un módulo que contenga 
las operaciones básicas de una calculadora: sumar, restar, multiplicar y dividir.

Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas.
Los resultados tenéis que mostrarlos por consola."""

from operaciones import sumar, restar, dividir, multiplicar


print(sumar.suma(2, 5))
print(restar.resta(5, 2))
print(multiplicar.multiplica(2, 4))
print(dividir.divide(7, 3))
