from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Esta ruta vacía representa la página de inicio
    # Otras rutas y vistas pueden ir aquí si es necesario

# Gestionar Proveedores
        path('crear_proveedor/', views.crear_proveedor, name='crear_proveedor'),
        path('proveedores/', views.lista_proveedores, name='lista_proveedores'),
        path('proveedores/editar/<int:proveedor_id>/', views.editar_proveedor, name='editar_proveedor'),
        path('checkout/', views.checkout, name='checkout'),

#Reserva
    path('guardar_reserva/', views.guardar_reserva, name='guardar_reserva'),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),

# Servicios
    path('crear_servicio/', views.crear_servicio, name='crear_servicio'),
    path('lista_servicios/', views.lista_servicios, name='lista_servicios'),
    path('editar_servicio/<int:id_servicio>/', views.editar_servicio, name='editar_servicio'),




]
