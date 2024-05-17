import random

# Variables
numero_aleatorio = random.randint(1, 25)
intentos = 0

# Bucle
while intentos < 5:
    # Input
    adivinanza = int(input("Adivina un número entre 1 y 25: "))
    intentos += 1

    # Condicionales
    if adivinanza < numero_aleatorio:
        print("Intenta un número más alto.")
    elif adivinanza > numero_aleatorio:
        print("Intenta un número más bajo.")
    else:
        print("¡Felicidades, lo has adivinado!")
        break

# Operadores lógicos
if intentos == 5:
    print("Lo siento, has agotado tus intentos. El número era " + str(numero_aleatorio))

# Operadores aritméticos y asignación de valores
puntuacion = 10 - intentos
print("Tu puntuación final es: " + str(puntuacion))