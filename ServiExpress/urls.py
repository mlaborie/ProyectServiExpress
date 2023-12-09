from django.urls import path
from . import views


urlpatterns = [
    path('', views.base, name='base'),  # Esta ruta vacía representa la página de inicio
    # Otras rutas y vistas pueden ir aquí si es necesario


#menu_administrador

        path('IndexAdministratoris/',views.IndexAdministratoris,name='IndexAdministratoris'),
        path('generar_orden_compra/', views.generar_orden_compra, name='generar_orden_compra'),
        path('lista_ordenes_de_compra/', views.lista_ordenes_de_compra, name='lista_ordenes_de_compra'),
        path('orden_de_compra/<int:orden_id>/pdf/', views.detalle_orden_de_compra, name='detalle_orden_de_compra_pdf'),

    # Gestionar Proveedores
        path('crear_proveedor/', views.crear_proveedor, name='crear_proveedor'),
        path('proveedores/', views.lista_proveedores, name='lista_proveedores'),
        path('proveedores/editar/<int:proveedor_id>/', views.editar_proveedor, name='editar_proveedor'),
        path('checkout/', views.checkout, name='checkout'),

    # Servicios
        path('crear_servicio/', views.crear_servicio, name='crear_servicio'),
        path('lista_servicios/', views.lista_servicios, name='lista_servicios'),
        path('editar_servicio/<int:id_servicio>/', views.editar_servicio, name='editar_servicio'),
    
    # Producto
        path('crear_producto/', views.crear_producto, name='crear_producto'),
        path('lista_productos/', views.lista_productos, name='lista_productos'),
        path('editar-producto/<int:id_producto>/', views.editar_producto, name='editar_producto'),
    
    
        path('crear_cliente/', views.crear_cliente, name='crear_cliente'),
        path('crear_empleado/', views.crear_empleado, name='crear_empleado'),
        path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    
#menu_cliente

        path('menu_cliente/',views.menu_cliente,name='menu_cliente'),
        path('index10/',views.index10, name='index10'),
        path('index30/',views.index30, name='index30'),
        path('index50',views.index50, name='index50'),

    #Reserva
        path('guardar_reserva/', views.guardar_reserva, name='guardar_reserva'),
        path('calendar/', views.CalendarView.as_view(), name='calendar'),

#menu_vendedor

        path('menu_vendedor/', views.menu_vendedor, name='menu_vendedor'),
        path('genear_boleta/', views.generar_boleta, name='generar_boleta')
        

]
