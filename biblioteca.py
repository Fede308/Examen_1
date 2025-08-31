from items import Libro, Revista, Periodico

class Biblioteca:
    def __init__(self):
        self.items = []

    def agregar_libro(self, titulo, autor, editorial):
        self.items.append(Libro(titulo, autor, editorial))

    def agregar_revista(self, titulo, autor, editorial, numero):
        self.items.append(Revista(titulo, autor, editorial, numero))

    def agregar_periodico(self, titulo, autor, editorial, fecha_publicacion):
        self.items.append(Periodico(titulo, autor, editorial, fecha_publicacion))

    def prestar_item(self, titulo):
        for item in self.items:
            if item.titulo == titulo:
                return item.prestar()
        return "Ítem no encontrado."

    def devolver_item(self, titulo):
        for item in self.items:
            if item.titulo == titulo:
                return item.devolver()
        return "Ítem no encontrado."

    def buscar_por_autor(self, autor):
        return [item for item in self.items if item.buscar_por_autor(autor)]

    def listar_items(self):
        if not self.items:
            print("No hay ítems en la biblioteca.")
        else:
            for item in self.items:
                print(item.mostrar_detalles())
