from random import randrange

def crearContrasenia():
    longitud = int(input("Ingrese la longitud deseada de su contraseña: "))
    if ( longitud < 8 ):
        print("La contraseña debe tener al menos 8 caracteres.")
        return crearContrasenia()
    
    clave = ""
    for _ in range(1, longitud):
        clave = clave + chr(randrange(0, 256))

    print(f"Su contraseña nueva es: {clave}")

crearContrasenia()