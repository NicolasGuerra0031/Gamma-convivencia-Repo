from django.contrib import admin
from django.urls import path, include  # ← include permite conectar otras apps

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),  # ← conecta con las rutas de la app "usuarios"
]
