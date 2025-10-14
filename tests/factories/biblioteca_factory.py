import factory
from apps.biblioteca.models import Biblioteca


class BibliotecaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Biblioteca

    nombre: str = factory.Faker("company")
    direccion: str = factory.Faker("address")
