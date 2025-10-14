from django.urls import path
from apps.usuario.views import UsuarioListCreateAPIView

urlpatterns = [
    path('usuarios/', UsuarioListCreateAPIView.as_view(), name='usuario-list-create'),
]
