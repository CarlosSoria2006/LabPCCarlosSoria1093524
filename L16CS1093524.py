#Carlos Soria - 1093524

import random 

print("Semana No. 16: Ejercicio 1")

lista = []

for x in range (10):
    lista.append(random.randint(0,10))

opcion = "a"

while opcion != "e":
    print ("Menú")
    print("a. Mostrar números", "b. Promedio", "c. Longitud", "d. Posición", sep="\n")
    opcion = input("Ingrese su opción: ")
    
    match opcion: 
        case "a": #opción mostrar números
            for x in range(len(lista)):
                print(f"No. {x}: {lista[x]}")
        case "b": 
            print("SUMATORIA")
            sumatoria = 0 
            for x in range (len(lista)):
                sumatoria += lista[x]       
            promedio = sumatoria / len(lista)
            print(f"---- Promedio: {promedio}") 
        case "c": 
            print(len(lista))
        case "d": 
            suma1 = 0 
            suma2 = 0 
            for x in range (len(lista)):
                if x % 2 == 0: 
                    suma1 = suma1 + lista[x]
                else: 
                    suma2 = suma2 + lista[x]
            print(f"la suma de las posiciones pares es {suma1}")
            print(f"la suma de las posiciones impares es {suma2}")


print("Semana No. 16: Ejercicio 2")

cantFilas = int(input("Ingrese la cantidad de filas: "))
cantCols = int(input("Ingrese la cantidad de columnas: "))

matriz = [[0 for x in range (cantCols)] for y in range (cantFilas)]
mayor = 0 
menor = float('inf')
pares = 0
impares = 0

for xFilas in range (cantFilas):
    for xCols in range (cantCols): 
        matriz [xFilas][xCols] = random.randint(0,1000)

        # Comparación Mayor
        if (matriz[xFilas][xCols] > mayor): 
            mayor = matriz[xFilas][xCols]

          # Comparación Menor
        if matriz[xFilas][xCols] < menor:
            menor = matriz[xFilas][xCols]

        # Conteo de pares e impares
        if matriz[xFilas][xCols] % 2 == 0:
            pares += 1
        else:
            impares += 1
            
print(matriz)
print(f"El número mayor es {mayor}")
print(f"El número menor es {menor}")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")