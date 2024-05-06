import random

# Función para solicitar la información del niño
def obtener_informacion_nino():
    print("¡Bienvenido al programa de cuentos infantiles!")
    nombre = input("Por favor, ingresa el nombre del niño: ")
    edad = input("Por favor, ingresa la edad del niño: ")
    print("\n¡Gracias! Ahora elige su color favorito:")
    print("1. Rojo")
    print("2. Azul")
    print("3. Verde")
    print("4. Amarillo")
    print("5. Rosa")
    color_opcion = int(input("Ingrese el número correspondiente al color favorito: "))
    colores = {1: "Rojo", 2: "Azul", 3: "Verde", 4: "Amarillo", 5: "Rosa"}
    color_favorito = colores[color_opcion]
    return nombre, edad, color_favorito

# Función para generar el cuento
def generar_cuento(nombre, edad, color_favorito):
    print("\n¡Hola " + nombre + "! Vamos a comenzar nuestro cuento.")
    print("\nTítulo: La aventura de " + nombre)
    for i in range(1, 6):
        print("\nSecuencia " + str(i) + ":")
        mostrar_panel(color_favorito)
        mostrar_narrativa(nombre, int(edad), color_favorito, i)
        if i < 5:
            if not continuar():
                print("\n¡Gracias por participar!")
                return
    print("\n¡Felicidades! Has completado la historia.")
    print("\n¡Espero que hayas disfrutado el cuento, " + nombre + "! ¡Hasta luego!")

# Función para mostrar el panel con diseño poligonal
def mostrar_panel(color_favorito):
    print("\nPanel:")
    # Aquí iría la lógica para mostrar el panel con diseño poligonal
    # No se implementa aquí ya que se trabajaran por aparte

# Función para mostrar la narrativa
def mostrar_narrativa(nombre, edad, color_favorito, secuencia):
    print("\nNarrativa:")
    narrativas = [
        nombre + " era un niño muy valiente que vivía en un pueblo muy muy lejano, él tenía " + str(edad) + " años. ",
        "Un día, él subió a la colina que tapaba todas las tardes con su gran sombra por el sol, y al llegar hasta lo más alto, " + nombre + " se encontró con un dragón que estaba dormido, el dragón era de color " + color_favorito + ". ",
        "El dragón lo olfateó y en ese momento voló por toda la colina y volvió con " + nombre + ", el dragón a pesar de ser malhumorado, al ver que era un niño muy educado y valiente por no temer de él, lo subió a su lomo y volaron juntos por todo el cielo azul",
        "Luego, en una de sus muchas aventuras, " + nombre + " encontró un pergamino pérdido, que les daba pistas y un mapa para encontrar un cofre lleno de monedas de oro. ",
        "Juntos fueron volando por todos los cielos buscando el cofre. " + nombre + " muy emocionado y eufórico le pareció ver algo brillante desde el cielo y se parecía al lugar donde marcaba el mapa, bajaron y lograron encontrar el tesoro, ambos muy felicices agradecieron por haberse encontrado en aquella colina y se volvieron mejores amigos por siempre y para siempre! End. "
    ]
    narrativa = narrativas[secuencia-1]
    print(narrativa)
    print()
    

# Función para continuar a la siguiente secuencia
def continuar():
    respuesta = input("\n¿Quieres continuar a la siguiente secuencia? (SI/NO): ")
    return respuesta.upper() == "SI"

# Programa principal
def main():
    nombre, edad, color_favorito = obtener_informacion_nino()
    generar_cuento(nombre, edad, color_favorito)

if __name__ == "__main__":
    main()
