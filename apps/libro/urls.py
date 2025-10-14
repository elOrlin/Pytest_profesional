from django.urls import path
from apps.libro.views import LibroListCreateAPIView, BorrowLibroAPIView

urlpatterns = [
    path('libros/', LibroListCreateAPIView.as_view(), name='libro-list-create'),
    path('libros/borrow/', BorrowLibroAPIView.as_view(), name='libro-borrow'),
]
