def contar_vocales(frase):
    cantidad_vocales = 0
    
    for caracter in frase:
        if caracter in ["a", "e", "i", "o", "u"]:
            cantidad_vocales = cantidad_vocales + 1

    return cantidad_vocales
            
            
frase_seleccionada = str(input("Escriba una frase para contar sus vocales: "))
cantidad_total = contar_vocales(frase_seleccionada)

print(f"La cantidad total de vocales es: {cantidad_total}")