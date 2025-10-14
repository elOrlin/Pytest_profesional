from contextlib import contextmanager


class UsuarioContextManager:
    """Lógica de negocio para usuarios"""

    def get_all_users(self):
        from apps.usuario.models import Usuario
        return Usuario.objects.all()

    def create_user(self, nombre: str, email: str, telefono=None):
        from apps.usuario.models import Usuario
        user = Usuario.objects.create(
            nombre=nombre,
            email=email,
            telefono=telefono or ""
        )
        return user

    @contextmanager
    def temporary_activo(self, user):
        """Activa temporalmente al usuario"""
        original = user.activo
        user.activo = True
        user.save()
        try:
            yield user
        finally:
            user.activo = original
            user.save()
