# apps/libro/models.py
from django.db import models
from apps.usuario.models import Usuario
from .context_manager import LibroContextManager


class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    disponible = models.BooleanField(default=True)

    # 👇 Relación: quién tomó prestado el libro
    borrower = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="libros_prestados"
    )

    objects = LibroContextManager()

    def __str__(self):
        return self.titulo
