def es_primo(numero, iteration = 2):
    if ( numero in [0, 1] ): 
        return False
        
    if ( iteration == numero ):
        return True
    
    if ( numero % iteration == 0 ):
        return False

    return es_primo(numero, iteration + 1)



numeroIngresado = int(input("Ingrese un número entero: "))
print(f"El numero es primo? {es_primo(numeroIngresado)}")

    