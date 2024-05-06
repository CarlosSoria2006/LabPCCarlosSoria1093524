import turtle
import random

# Configuración de la ventana
wn = turtle.Screen()
wn.bgcolor("lightblue")  # Color de fondo celeste
wn.title("Dibujando nubes en el cielo")

# Configuración del objeto turtle
t = turtle.Turtle()
t.speed(0)  # Configura la velocidad del dibujo

# Función para dibujar una nube
def dibujar_nube(x, y, radio):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(radio)
    t.end_fill()

# Función para dibujar un pájaro
def dibujar_pajaro(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.circle(5)  # Cuerpo del pájaro
    t.end_fill()
    t.setheading(45)
    t.forward(15)  # Lado derecho del triángulo
    t.setheading(-135)
    t.forward(15 * 2 ** 0.5)  # Base del triángulo
    t.setheading(45)
    t.forward(15)  # Lado izquierdo del triángulo
    t.penup()

# Dibujar nubes
for _ in range(35):
    x = random.randint(-300, 300)
    y = random.randint(50, 250)
    radio = random.randint(20, 60)
    dibujar_nube(x, y, radio)

# Dibujar pájaro
dibujar_pajaro(100, -100)

# Ocultar turtle y terminar
t.hideturtle()
wn.mainloop()
