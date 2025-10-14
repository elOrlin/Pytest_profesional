import factory
from apps.libro.models import Libro


class LibroFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Libro

    titulo: str = factory.Faker("sentence", nb_words=3)
    autor: str = factory.Faker("name")
    disponible: bool = True
    borrower: bool = None
