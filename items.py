class ItemBiblioteca:
    def __init__(self, titulo, autor, editorial):
        self._titulo = titulo
        self._autor = autor
        self._editorial = editorial
        self._prestado = False

    @property
    def titulo(self):
        return self._titulo

    def prestar(self):
        if not self._prestado:
            self._prestado = True
            return f'Ítem "{self._titulo}" prestado.'
        return f'Ítem "{self._titulo}" ya está prestado.'

    def devolver(self):
        if self._prestado:
            self._prestado = False
            return f'Ítem "{self._titulo}" devuelto.'
        return f'Ítem "{self._titulo}" no estaba prestado.'

    def buscar_por_autor(self, autor):
        return self._autor == autor

    def mostrar_detalles(self):
        return f"Título: {self._titulo}, Autor: {self._autor}, Editorial: {self._editorial}"


class Libro(ItemBiblioteca):
    def mostrar_detalles(self):
        return f"[Libro] Título: {self._titulo}, Autor: {self._autor}, Editorial: {self._editorial}"


class Revista(ItemBiblioteca):
    def __init__(self, titulo, autor, editorial, numero):
        super().__init__(titulo, autor, editorial)
        self._numero = numero

    def mostrar_detalles(self):
        return f"[Revista] Título: {self._titulo}, Número: {self._numero}, Autor: {self._autor}, Editorial: {self._editorial}"


class Periodico(ItemBiblioteca):
    def __init__(self, titulo, autor, editorial, fecha_publicacion):
        super().__init__(titulo, autor, editorial)
        self._fecha_publicacion = fecha_publicacion

    def mostrar_detalles(self):
        return f"[Periódico] Título: {self._titulo}, Fecha: {self._fecha_publicacion}, Autor: {self._autor}, Editorial: {self._editorial}"
