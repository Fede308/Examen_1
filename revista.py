class Revista(ItemBiblioteca):
    def __init__(self, titulo, autor, numero):
        super().__init__(titulo, autor) # Herencia: Llama al constructor de la clase base
        self._numero = numero # Encapsulamiento: atributo protegido

    def mostrar_detalles(self):
        # Polimorfismo: Implementación específica para Revista
        estado = "Prestado" if self._prestado else "Disponible"
        return f"Revista: {self._titulo}, Autor: {self._autor}, Número: {self._numero}, Estado: {estado}"

    # Getter para acceder al atributo protegido (Encapsulamiento)
    def get_numero(self):
        return self._numero