import pytest
from tests.fixtures.libro_fixtures import libro_creation


def test_libro_creation(libro_creation):
    assert libro_creation.titulo
    assert libro_creation.autor
    assert libro_creation.disponible is True


def test_libro_borrowed(libro_creation):
    from apps.libro.context_manager import LibroContextManager
    cm = LibroContextManager()

    with cm.mark_as_borrowed(libro_creation) as libro:
        # Dentro del contexto, el libro está marcado como prestado
        assert not libro.disponible

    # Fuera del contexto, el libro vuelve a estar disponible
    assert libro.disponible
