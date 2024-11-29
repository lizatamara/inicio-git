"""

Ejercicio 7: Número par o impar
Pide al usuario un número y determina si es par o impar.

"""


numerosPar = 0
numerosImpar = 0

while True:
    numero = int(input("ingrese un número "))
    if numero % 2 == 0:
        print("el número es par")
        numerosPar += 1
    else:
        print("el número es impar")
        numerosImpar +=1
    opcion = input("si desea continuar presione enter, sino escriba stop")
    if opcion == "stop":
        break
    
print(numerosPar)
print(numerosImpar)
    
