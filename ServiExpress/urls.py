from django.urls import path
from . import views

urlpatterns = [
    # Otras URL de tu aplicación aquí

    

    path('', views.index, name='home'),  # Esta línea configura la página de inicio

    path('home/', views.home, name='incio'),    
]
