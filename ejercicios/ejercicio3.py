"""
Ejercicio 3: Contar vocales en una palabra
Pide al usuario una palabra y cuenta cuántas vocales tiene.

"""
palabra = input("Escribe una palabra: ")
contador = 0
vocales = ["a", "e", "i", "o", "u"]
 
for letra in palabra:
    if letra in vocales:
        contador += 1
        
print(f"la palabra {palabra} tiene {contador} vocales")
        

