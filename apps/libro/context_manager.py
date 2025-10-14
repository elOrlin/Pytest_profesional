from contextlib import contextmanager
from apps.usuario.models import Usuario


class LibroContextManager:
    """Lógica de negocio de libros"""

    def get_all_libros(self):
        from apps.libro.models import Libro
        return Libro.objects.all()

    def create_libro(self, titulo: str, autor: str, disponible: bool, borrower=None):
        from apps.libro.models import Libro
        return Libro.objects.create(titulo=titulo, autor=autor, disponible=disponible, borrower=borrower)

    @contextmanager
    def mark_as_borrowed(self, libro):
        libro.disponible = False
        try:
            yield libro
        finally:
            libro.disponible = True

    @contextmanager
    def borrow_libro(self, user: Usuario, libro):
        if not libro.disponible:
            raise ValueError("El libro no está disponible")
        libro.borrower = user
        libro.disponible = False
        libro.save()
        try:
            yield libro
        finally:
            libro.borrower = None
            libro.disponible = True
            libro.save()

    @contextmanager
    def mark_as_borrowed_temporal(self, libro):
        libro.disponible = False
        libro.save()
        try:
            yield libro
        finally:
            libro.disponible = True
            libro.save()
