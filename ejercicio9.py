from random import randrange


print("¡Adiviná el número entre 1 y 100!")

cantidad_intentos = 0
numero_aleatorio = randrange(0, 100)
numero_seleccionado = None

while numero_seleccionado != numero_aleatorio:
    cantidad_intentos = cantidad_intentos + 1
    numero_seleccionado = int(input("Ingresá tu intento: "))
    
    if ( numero_seleccionado > numero_aleatorio ): 
        print("El número es menor.")

    if ( numero_seleccionado < numero_aleatorio ): 
        print("El número es mayor.")

print(f"¡Felicitaciones! Has adivinado el número en {cantidad_intentos} intentos.")
