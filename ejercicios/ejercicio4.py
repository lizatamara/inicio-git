"""
Ejercicio 4: Encontrar el número mayor
Dado un listado de números, encuentra el mayor usando un ciclo y un condicional.

"""

numeros = [3, 4, 5, 105, 23, 2, 76]
aux = 0

for x in numeros:
    if x > aux:
        aux = x
print(aux)
    