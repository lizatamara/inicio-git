"""
Ejercicio 5: Contar hasta que el usuario lo detenga
Usa un ciclo while para imprimir números empezando desde 1, hasta que el usuario escriba stop.


"""
numero = 1

while True:
    print(numero)
    numero += 1
    opcion = input("para seguir presione enter, para detener escriba stop ")
    if opcion == "stop":
        break
        

    