from django.urls import path
from . import views

urlpatterns = [
        
        path('', views.base, name='base'),  # Esta ruta vacía representa la página de inicio
    # Otras rutas y vistas pueden ir aquí si es necesario
        path('base/', views.base, name='base'),
# Gestionar Proveedores
        path('crear_proveedor/', views.crear_proveedor, name='crear_proveedor'),
        path('proveedores/', views.lista_proveedores, name='lista_proveedores'),
        path('proveedores/editar/<int:proveedor_id>/', views.editar_proveedor, name='editar_proveedor'),
        path('checkout/', views.checkout, name='checkout'),
        path('boleta/<int:boleta_id>/', views.boleta, name='generar_boleta'),
]
