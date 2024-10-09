class Libro:
    titulo = ""
    autor = ""
    anio_publicacion = 0
    numero_paginas = 0

    def __init__(self, titulo, autor, anio_publicacion, numero_paginas) -> None:
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.numero_paginas = numero_paginas


    def mostrar_informacion(self) -> str:
        return f"INFORMACIÓN: \nTitulo: {self.titulo} \nAutor: {self.autor} \nAño de publicación: self.anio_publicacion \nNúmero de páginas: {self.numero_paginas}"
    
libro = Libro("Blanca Olmedo", "Lucila Gamero de Medina", 1900, 400)

print(libro.mostrar_informacion())