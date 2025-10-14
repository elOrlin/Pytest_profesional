from rest_framework import generics
from rest_framework.response import Response
from apps.libro.models import Libro
from apps.libro.serializers import LibroSerializer
from apps.libro.context_manager import LibroContextManager
from apps.usuario.models import Usuario


class LibroListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = LibroSerializer

    def get_queryset(self):
        cm = LibroContextManager()
        return cm.get_all_libros()

    def perform_create(self, serializer):
        cm = LibroContextManager()
        cm.create_libro(**serializer.validated_data)


class BorrowLibroAPIView(generics.GenericAPIView):
    serializer_class = LibroSerializer

    def post(self, request):
        user = Usuario.objects.first()  # Ejemplo: usar request.user
        libro = Libro.objects.first()   # Ejemplo
        cm = LibroContextManager()
        try:
            with cm.borrow_libro(user, libro) as borrowed:
                serializer = LibroSerializer(borrowed)
                return Response(serializer.data)
        except ValueError as e:
            return Response({"error": str(e)}, status=400)
