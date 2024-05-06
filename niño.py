import turtle

# Configuración inicial
turtle.setup(800, 600)
turtle.speed(0)
turtle.hideturtle()

# Función para dibujar un círculo
def draw_circle(color, x, y, radius):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

# Función para dibujar un rectángulo
def draw_rectangle(color, x, y, width, height):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x - width / 2, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

# Función para dibujar un triángulo
def draw_triangle(color, x, y, size):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(size)
        turtle.right(120)
    turtle.end_fill()

# Dibujar la cara
def draw_face():
    # Cabeza
    draw_circle("#F9C28B", 0, 0, 50)
    
    # Ojos
    draw_circle("white", -20, 10, 8)
    draw_circle("white", 20, 10, 8)
    draw_circle("black", -20, 10, 3)
    draw_circle("black", 20, 10, 3)
    
    # Boca
    turtle.penup()
    turtle.goto(-15, -10)
    turtle.pendown()
    turtle.setheading(-60)
    turtle.circle(15, 120)

# Dibujar el niño completo
def draw_kid():
    # Cuerpo
    draw_rectangle("#7EC8E3", 0, -100, 50, 100)
    # Brazos
    draw_rectangle("#7EC8E3", -70, -60, 20, 80)
    draw_rectangle("#7EC8E3", 70, -60, 20, 80)
    # Piernas
    draw_rectangle("#7EC8E3", -20, -200, 20, 100)
    draw_rectangle("#7EC8E3", 20, -200, 20, 100)
    # Cara
    draw_face()

# Dibujar el niño completo
draw_kid()

# Mostrar el dibujo y esperar
turtle.done()
