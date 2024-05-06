# EJERCICIO 1 CARLOS SORIA

import math 

print("Semana No 15. Ejercicio 1")

print("Menú", "a. Área de un triángulo",
"b. Área de un cuadrado", 
"c. Área de un rectángulo", 
"d. Área de un circulo", 
sep = "\n")

menu = input("Ingresa tu opción elegida \n")

def Areatriangulo(base,altura): 
    Paso1 = base * altura
    Total = Paso1 /2
    return Total


def Areacuadrado(base): 
    Total = base**2
    return Total


def Arearectangulo(base,altura): 
    Total = base * altura
    return Total


def Areacirculo(radio): 
    Radio2 = radio**2
    Total = math.pi * Radio2 
    return Total

match menu: 
    case "a": 
        base = int(input("Ingresa un número para la base: "))
        altura = int(input("Ingresa un número para la altura: "))
        print("El área total del triángulo es: " + str(Areatriangulo(base,altura)))

    case "b":
        base = int(input("Ingresa el lado del cuadrado: "))
        print("El área total del cuadrado es: " + str(Areacuadrado(base)))

    case "c": 
        base = int(input("Ingresa un número para la base: "))
        altura = int(input("Ingresa un número para la altura: "))
        print("El área total del triángulo es: " + str(Arearectangulo(base,altura)))

    case "d":
        radio = int(input("Ingresa el radio del circulo: "))
        print("El área total del triángulo es: " + str(Areacirculo(radio)))

    case "":
        print("ERROR, ingresa una opción válida")

    case int:
        print("ERROR, ingresa una opción válida")
    
# EJERCICIO 2 CARLOS SORIA   

print("Semana No 15. Ejercicio 2")

x = 0
y = 0
def MoverPosicion(cantx, canty): 
    global x,y
    x += cantx
    y += canty

opcion = "a" 
while(opcion != "e"):
    print("Menú")
    print("a. Sube", "b. Baja", "c. Izquierda", "d. Derecha", "e. Salir", sep = "\t\n" )
    opcion = input("Ingrese su opción\n ")

    match opcion: 
        case "a": 
            MoverPosicion(0,1)
        case "b": 
            MoverPosicion(0,-1)
        case "c": 
            MoverPosicion(-1,0)
        case "d": 
            MoverPosicion(1,0)
        case "x": 
            x = 0
            y = 0

    print(f"La posición actual es: [{x}][{y}]")