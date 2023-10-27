from django.urls import path
from . import views

urlpatterns = [
    # Otras URL de tu aplicación aquí

    path('', views.index, name='index'),  # Esta línea configura la página de inicio

    path('modulos/', views.modulos_view, name='modulos'),

    path('FormularioReserva/', views.FormularioReserva, name='FormularioReserva'),

    path('reservas/', views.ReservaExitosa, name='ReservaExitosa'),

    path('BuscarReserva/', views.BuscarReserva, name='BuscarReserva'),

    path('Login/', views.Login, name='Login'), 
    path('login/', views.login_view, name='login'),  # URL para la vista de inicio de sesión
    path('logout/', views.logout_view, name='logout'),  # URL para la vista de cierre de sesión
    

        path('crear_proveedor/', views.crear_proveedor, name='crear_proveedor'),




    #uwu
    path('administrar-usuarios/', views.administrar_usuarios, name='administrar_usuarios'),
    path('crear-usuario/', views.crear_usuario, name='crear_usuario'),
    path('deshabilitar-usuario/', views.deshabilitar_usuario, name='deshabilitar_usuario'),
        path('habilitar-usuario/', views.habilitar_usuario, name='habilitar_usuario'),
        path('editar-usuario/<int:user_id>/', views.editar_usuario, name='editar_usuario'),




    
]
