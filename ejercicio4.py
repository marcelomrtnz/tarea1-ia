class Calculadora:

    @staticmethod
    def sumar(a, b) -> float:
        return a + b
    
    @staticmethod
    def restar(a, b) -> float:
        return a - b

    @staticmethod
    def multiplicar(a, b) -> float:
        return a * b
    
    @staticmethod
    def dividir(a, b):
        if (b == 0):
            print("NO SE PUEDE DIVIDIR ENTRE 0.")
        else:
            return a / b
        
    def encender(self):
        opcion = input(f"Bienvenido a su calculadora de preferencia. \nDigite el inciso de la operación que desea realizar: \na) suma \nb) resta \nc) multiplicación \nd) división \nSu opción: ")
        if opcion not in ["a", "b", "c", "d"]:
            print("\n\nDebe seleccionar uno de los incisos mencionados.\n\n")
            return self.encender()

        valor1 = float(input("Ingrese su primer valor: "))
        valor2 = float(input("Ingrese su segundo valor: "))

        resultado = None

        match opcion:
            case "a":
                resultado = self.sumar(valor1, valor2)
            case "b":
                resultado = self.restar(valor1, valor2)
            case "c":
                resultado = self.multiplicar(valor1, valor2)
            case "d":
                resultado = self.dividir(valor1, valor2)

        print(f"Su resultado es: {resultado}")
            


calculadora = Calculadora()

calculadora.encender()

