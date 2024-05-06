import turtle

# Configuración de la ventana
wn = turtle.Screen()
wn.setup(width=600, height=400)
wn.bgcolor("beige")
wn.title("Pergamino del tesoro")

# Dibujar el pergamino
pen = turtle.Turtle()
pen.penup()
pen.goto(-200, 150)
pen.pendown()
pen.color("tan")
pen.begin_fill()
pen.forward(400)
pen.right(90)
pen.forward(300)
pen.right(90)
pen.forward(400)
pen.right(90)
pen.forward(300)
pen.end_fill()

# Dibujar la "X" del tesoro
pen.penup()
pen.goto(-10, -60)
pen.pendown()
pen.color("red")
pen.width(3)
pen.setheading(45)
pen.forward(30)
pen.backward(60)
pen.forward(30)
pen.left(90)
pen.forward(30)
pen.backward(60)

# Dibujar la ubicación del buscador del tesoro
pen.penup()
pen.goto(-180, 130)
pen.pendown()
pen.dot(10, "black")

# Dibujar las líneas que apuntan al tesoro
pen.penup()
pen.goto(-180, 130)
pen.pendown()
pen.setheading(pen.towards(-10, -60))
pen.forward(50)
pen.backward(50)
pen.penup()
pen.goto(-180, 130)
pen.pendown()
pen.setheading(pen.towards(-10, -60))
pen.left(30)
pen.forward(50)
pen.backward(50)
pen.penup()
pen.goto(-180, 130)
pen.pendown()
pen.setheading(pen.towards(-10, -60))
pen.right(30)
pen.forward(50)
pen.backward(50)

# Escribir "Tesoro"
pen.penup()
pen.goto(-40, -100)
pen.color("black")
pen.write("Tesoro", font=("Arial", 16, "bold"))

# Ocultar la pluma
pen.hideturtle()

# Mantener la ventana abierta
wn.mainloop()
