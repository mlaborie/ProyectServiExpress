from django.urls import path
from . import views

urlpatterns = [
    # Otras URL de tu aplicación aquí

    path('', views.index, name='index'),  # Esta línea configura la página de inicio

    path('modulos/', views.modulos_view, name='modulos'),
    
]
