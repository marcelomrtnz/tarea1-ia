def fibonacci(numero_actual, numero_siguiente, ciclos, iteracion):
    print(numero_actual)
    
    if iteracion < ciclos:
        fibonacci(numero_siguiente, numero_actual + numero_siguiente, ciclos, iteracion + 1)


ciclos = int(input("Ingrese el número de términos: "))
print("\nSERIE DE FIBONACCI:\n")
fibonacci(0, 1, ciclos, 1)