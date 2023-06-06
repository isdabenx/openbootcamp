"""En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de
una lista pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos
mediante reduce."""

from functools import reduce
from typing import List

def suma_impares(numeros: List) -> int:
    """Suma impares"""
    return reduce(lambda a, b: a + b, filter(lambda x: x % 2 != 0, numeros))

print(suma_impares([3,45,2,1,3,5,6,7,10,22,5,100]))
