from django.db import models
from apps.libro.models import Libro
from .context_manager import BibliotecaContextManager


class Biblioteca(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    libros = models.ManyToManyField("libro.Libro", blank=True)

    objects = BibliotecaContextManager()

    def __str__(self):
        return self.nombre
