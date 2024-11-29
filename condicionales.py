edad = 25

nombre = "Alejandro"

if edad >= 18 and nombre != "Alejandro":
        print("bienvenida")
        print("hola")
elif edad >= 10:
    print("ve a la sala de juegos")
else:
    print("adios no vuelvas")
    
    
"""

genera un programa en python que le pregunte al usuario por su pais y le responda con un saludo tipico
usando solo condicionales

colombia: hola parce
chile: buena po
venezuela: hola chamo

"""

pais = input("ingressa tu país: ")

if pais == "colombia":
    print("hola parce")
elif pais == "chile":
    print("buena po")
elif pais == "venezuela":
    print("hola chamo")
else:
    print("hola")


"""

desarrolla un programa que reciba 3 numeros e imprima el numero mayor
solo utiliza condicionales



"""

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))
num4 = 0

if num1 > num2:
    num4 = num1
elif num2 > num1:
    num4 = num2
else:
    num4 = num3
    
print(f"el numero mayor es {num4}")

    
