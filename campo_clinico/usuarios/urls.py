from django.urls import path
from . import views  # ← importa las funciones que mostrarán contenido

urlpatterns = [
    path('', views.login_view, name='login'),  # ← ruta principal que muestra la vista de login
]
