"""
Ejercicio 8: Números hasta N
Pide al usuario un número N y usa un ciclo for para imprimir todos los números desde 1 hasta N.

"""

numero = int(input("ingrese un numero "))



rango = range(numero)

for x in rango:
    print(x+1)