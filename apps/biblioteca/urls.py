from django.urls import path
from apps.biblioteca.views import BibliotecaListCreateAPIView, AddLibroAPIView

urlpatterns = [
    path('bibliotecas/', BibliotecaListCreateAPIView.as_view(), name='biblioteca-list-create'),
    path('bibliotecas/add-libro/', AddLibroAPIView.as_view(), name='biblioteca-add-libro'),
]
