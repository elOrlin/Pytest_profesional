# tests/factories/usuario_factory.py
import factory
from faker import Faker
from apps.usuario.models import Usuario  # Importa SOLO tu modelo real

fake = Faker()


class UsuarioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Usuario
        django_get_or_create = ("email",)

    email = factory.LazyAttribute(lambda _: fake.unique.email())
    telefono = factory.LazyAttribute(lambda _: fake.msisdn())
    nombre = factory.LazyAttribute(lambda _: fake.first_name())
    apellido = factory.LazyAttribute(lambda _: fake.last_name())
