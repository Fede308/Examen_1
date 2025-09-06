class Periodico(ItemBiblioteca):
    def __init__(self, titulo, autor, fecha):
        super().__init__(titulo, autor) # Herencia: Llama al constructor de la clase base
        self._fecha = fecha # Encapsulamiento: atributo protegido

    def mostrar_detalles(self):
        # Polimorfismo: Implementación específica para Periodico
        estado = "Prestado" if self._prestado else "Disponible"
        return f"Periódico: {self._titulo}, Autor: {self._autor}, Fecha: {self._fecha}, Estado: {estado}"

    # Getter para acceder al atributo protegido (Encapsulamiento)
    def get_fecha(self):
        return self._fecha


