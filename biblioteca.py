class ItemBiblioteca:
    def __init__(self, titulo, autor):
        self._titulo = titulo  # Encapsulamiento: atributo protegido
        self._autor = autor    # Encapsulamiento: atributo protegido
        self._prestado = False # Encapsulamiento: atributo protegido

    def __str__(self):
        return f"Título: {self._titulo}, Autor: {self._autor}"

    def prestar(self):
        if not self._prestado:
            self._prestado = True
            return f'"{self._titulo}" prestado.'
        else:
            return f'"{self._titulo}" ya está prestado.'

    def devolver(self):
        if self._prestado:
            self._prestado = False
            return f'"{self._titulo}" devuelto.'
        else:
            return f'"{self._titulo}" no estaba prestado.'

    def buscar_por_autor(self, autor):
        return self._autor.lower() == autor.lower() # Búsqueda sin distinción de mayúsculas/minúsculas

    def mostrar_detalles(self):
        # Polimorfismo: Este método será sobrescrito en las subclases
        raise NotImplementedError("Subclase debe implementar este método abstracto")

    # Getters para acceder a los atributos protegidos (Encapsulamiento)
    def get_titulo(self):
        return self._titulo

    def get_autor(self):
        return self._autor

    def is_prestado(self):
        return self._prestado