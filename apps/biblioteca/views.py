from rest_framework import generics
from rest_framework.response import Response
from apps.biblioteca.models import Biblioteca
from apps.biblioteca.serializers import BibliotecaSerializer
from apps.biblioteca.context_manager import BibliotecaContextManager
from apps.libro.models import Libro


class BibliotecaListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = BibliotecaSerializer

    def get_queryset(self):
        cm = BibliotecaContextManager()
        return cm.get_all_bibliotecas()

    def perform_create(self, serializer):
        cm = BibliotecaContextManager()
        cm.create_biblioteca(**serializer.validated_data)


class AddLibroAPIView(generics.GenericAPIView):
    serializer_class = BibliotecaSerializer

    def post(self, request):
        biblioteca = Biblioteca.objects.first()  # Ejemplo
        libro = Libro.objects.first()           # Ejemplo
        cm = BibliotecaContextManager()
        with cm.add_libro_temporal(biblioteca, libro) as libro_added:
            serializer = BibliotecaSerializer(biblioteca)
            return Response(serializer.data)