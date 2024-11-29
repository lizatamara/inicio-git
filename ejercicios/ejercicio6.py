"""
Ejercicio 6: Adivina el número
Crea un programa donde el usuario adivine un número entre 1 y 10.

"""
import random

numero = int(input("adivine un número del 1 al 10 "))
random = random.randint(1, 10)

if numero == random:
    print("adivinaste!")
else:
    print(f"perdiste, el número era {random}")


