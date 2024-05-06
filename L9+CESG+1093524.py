print("Ejercicio 1: operaciones aritméticas")
numero1 = int(input("Ingresa un numero: "))
numero2 = int(input("Ingresa otro numero: "))

suma = numero1 + numero2
resta =  numero1 - numero2
multiplicación = numero1 * numero2 
división = numero1 / numero2 
divisiónentera = numero1 // numero2
divisiónmodular = numero1 % numero2 

print(f"La suma total es = ", suma) 
print(f"La diferencia es =", resta)
print(f"El producto es =", multiplicación) 
print(f"La división es =", división)
print(f"La división entera es =", divisiónentera) 
print(f"La división modular es =", divisiónmodular)

print("Ejercicio 2: operaciones booleanas")

igualdad = numero1 == numero2
diferentes = numero1 != numero2

print(numero1 == numero2, "=", igualdad )
print(numero1 != numero2, "=", diferentes)

print("Ejercicio 3: jerarquía de operaciones")

a = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número: "))
c = int(input("Ingrese un último número: "))

ope1 = a * b + c
ope2 = a * b + c * a 
ope3 = a / b + c
ope4 = 3*a + 2*b // c**2

print("La operación 1 es", ope1, ", la segunda es", ope2, ", la tercera es", ope3, "y la cuarta", ope4 )

print("Actividad 3")

print("Carlos Eduardo Soria - 1093524")

metros = int(input("Ingrese un número entero: "))

millas = metros / 1609
kilómetros = metros / 1000 
pies = metros * 3.28
pulgadas = metros * 39.3701

print("Resultado en millas es", millas, ", en kilómetros", kilómetros, ", en pies", pies, "y en pulgadas", pulgadas)

metros1 = int(input("Ingrese otro número entero: "))

yardas = metros1 * 1.09361
pies1 = metros1 * 3.28
pulgadas1 = metros1 * 39.3701

print("Resultado en yardas", yardas, ", en pies", pies1, "y en pulgadas", pulgadas1)