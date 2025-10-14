import pytest
from tests.fixtures.biblioteca_fixtures import biblioteca_creation
from tests.fixtures.libro_fixtures import libro_creation
from apps.biblioteca.context_manager import BibliotecaContextManager


def test_biblioteca_creation(biblioteca_creation):
    assert biblioteca_creation.nombre
    assert biblioteca_creation.direccion


def test_add_libro_temporal(biblioteca_creation, libro_creation):
    cm = BibliotecaContextManager()
    with cm.add_libro_temporal(biblioteca_creation, libro_creation) as libro:
        assert libro in biblioteca_creation.libros.all()
    # Al salir del context manager, el libro ya no está
    assert libro_creation not in biblioteca_creation.libros.all()


def test_add_libro_permanente(biblioteca_creation, libro_creation):
    cm = BibliotecaContextManager()
    cm.add_libro_permanente(biblioteca_creation, libro_creation)
    assert libro_creation in biblioteca_creation.libros.all()
