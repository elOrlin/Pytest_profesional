from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.usuario.urls')),
    path('api/', include('apps.libro.urls')),
    path('api/', include('apps.biblioteca.urls')),
]

