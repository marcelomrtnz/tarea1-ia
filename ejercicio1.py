class Rectangulo:
    base = 0
    altura = 0

    def __init__(self, base, altura) -> None:
        self.base = base
        self.altura = altura

    def area(self) -> int:
        return self.base * self.altura
    
    def perimetro(self) -> int:
        return self.base + self.altura
    
rectangulo = Rectangulo(5, 3)

print(rectangulo.area())
print(rectangulo.perimetro())