lista = ["Dinosaurio", 23, True, 45.6, "Amazon"]

for x in lista:
    print(f"Elemento {x} tipo de dato {type(x)}")
    
# dada la siguiente lista imprime SOLO los números pares

numeros = [2, 45, 19, 13, 178]
    
    
for x in numeros:
    if x %2 == 0:
        print(f"{x}")