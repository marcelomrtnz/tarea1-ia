numero_seleccionado = int(input("Ingrese un número entero: "))

print(f"Tabla de multiplicar del {numero_seleccionado}")

for tabla in range(0, 10):
    print(f"{numero_seleccionado} x {tabla} = {tabla * numero_seleccionado}")