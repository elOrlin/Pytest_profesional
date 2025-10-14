from contextlib import contextmanager
from apps.libro.models import Libro


class BibliotecaContextManager:
    """Lógica de negocio de bibliotecas"""

    def get_all_bibliotecas(self):
        from apps.biblioteca.models import Biblioteca
        return Biblioteca.objects.all()

    def create_biblioteca(self, nombre: str, direccion: str):
        from apps.biblioteca.models import Biblioteca
        return Biblioteca.objects.create(nombre=nombre, direccion=direccion)

    @contextmanager
    def add_libro_temporal(self, biblioteca, libro: Libro):
        biblioteca.libros.add(libro)
        try:
            yield libro
        finally:
            biblioteca.libros.remove(libro)

    # Agregar método permanente
    def add_libro_permanente(self, biblioteca, libro: Libro):
        biblioteca.libros.add(libro)
        biblioteca.save()
        return libro

