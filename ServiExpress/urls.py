from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Esta ruta vacía representa la página de inicio
    # Otras rutas y vistas pueden ir aquí si es necesario

    
]
