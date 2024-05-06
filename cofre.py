import turtle

# Configuración de la ventana
wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.bgcolor("lightblue")
wn.title("Cofre del Tesoro")

# Dibujar la base del cofre
base = turtle.Turtle()
base.penup()
base.goto(-100, -100)
base.pendown()
base.color("#8B4513")  # Color café
base.begin_fill()
for _ in range(2):
    base.forward(200)
    base.left(90)
    base.forward(150)
    base.left(90)
base.end_fill()

# Dibujar los bordes de la base del cofre
base.penup()
base.goto(-100, -100)
base.pendown()
base.color("black")
for _ in range(2):
    base.forward(200)
    base.left(90)
    base.forward(150)
    base.left(90)

# Dibujar la línea central del cofre
base.penup()
base.goto(-100, 0)
base.pendown()
base.color("black")
base.forward(200)

# Dibujar el cerrojo del cofre
base.penup()
base.goto(-10, -5)
base.pendown()
base.color("black")
base.setheading(270)
base.forward(20)
base.right(90)
base.forward(20)
base.right(90)
base.forward(40)
base.right(90)
base.forward(20)
base.right(90)
base.forward(20)

# Dibujar el texto "Tesoro"
base.penup()
base.goto(-45, 60)
base.pendown()
base.color("black")
base.write("Tesoro", font=("Arial", 16, "bold"))

# Dibujar la "X" roja debajo del cofre
base.penup()
base.goto(0, -120)
base.pendown()
base.color("red")
base.write("X", font=("Arial", 16, "bold"))

# Dibujar las monedas alrededor del cofre
coin = turtle.Turtle()
coin.shape("circle")
coin.color("gold")
coin.penup()
coin.goto(-100, -150)

for _ in range(6):
    coin.stamp()
    coin.forward(40)

# Ocultar la pluma y mantener la ventana abierta
base.hideturtle()
coin.hideturtle()
wn.mainloop()
