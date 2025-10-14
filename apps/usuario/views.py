from rest_framework import generics
# from apps.usuario.models import Usuario
from apps.usuario.serializers import UsuarioSerializer
from apps.usuario.context_manager import UsuarioContextManager


class UsuarioListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        cm = UsuarioContextManager()
        return cm.get_all_users()

    def perform_create(self, serializer):
        cm = UsuarioContextManager()
        cm.create_user(**serializer.validated_data)
