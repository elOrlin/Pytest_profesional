import pytest
from tests.fixtures.usuario_fixtures import common_user_creation
from tests.fixtures.libro_fixtures import libro_creation
from tests.fixtures.biblioteca_fixtures import biblioteca_creation
from apps.biblioteca.context_manager import BibliotecaContextManager


def test_user_borrow_libro(common_user_creation, libro_creation, biblioteca_creation):
    """
    Simula un usuario que toma prestado un libro y lo agrega a la biblioteca.
    """
    # Marcamos libro como prestado
    from apps.libro.context_manager import LibroContextManager
    cm_libro = LibroContextManager()
    with cm_libro.mark_as_borrowed(libro_creation):
        # El libro sigue disponible dentro del context manager
        assert libro_creation.disponible is False
        # Lo agregamos a biblioteca temporalmente
        cm_biblio = BibliotecaContextManager()
        with cm_biblio.add_libro_temporal(biblioteca_creation, libro_creation) as libro:
            assert libro in biblioteca_creation.libros.all()
    # Al salir de ambos context managers
    assert libro_creation.disponible is True
    assert libro_creation not in biblioteca_creation.libros.all()


