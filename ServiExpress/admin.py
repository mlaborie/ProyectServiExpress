from django.contrib import admin
from .models import Cliente, Empleado, Factura, OrdenDeCompra, Producto, Proveedor, Reserva, Servicio, FacturaReserva, OrdenDeCompraEmpleado, OrdenDeCompraProducto, OrdenDeCompraProveedor, ReservaCliente

# Registra tus modelos aquí

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id_cliente', 'nombre', 'apellido', 'correo', 'telefono', 'direccion']

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['id_empleado', 'nombre', 'apellido', 'cargo', 'estado']

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ['id_factura', 'id_reserva', 'fecha', 'subtotal', 'iva', 'total']

@admin.register(OrdenDeCompra)
class OrdenDeCompraAdmin(admin.ModelAdmin):
    list_display = ['id_orden_de_pedido', 'id_proveedor', 'id_producto', 'cantidad', 'precio', 'empleado', 'comentario']

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id_producto', 'nombre', 'descripcion', 'precio']

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['id_proveedor', 'nombre', 'contacto', 'rubro']

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['id_reserva', 'id_cliente', 'fecha', 'hora', 'servicio', 'precio']

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ['id_servicio', 'nombre', 'descripcion', 'precio']

@admin.register(FacturaReserva)
class FacturaReservaAdmin(admin.ModelAdmin):
    list_display = ['factura', 'reserva']

@admin.register(OrdenDeCompraEmpleado)
class OrdenDeCompraEmpleadoAdmin(admin.ModelAdmin):
    list_display = ['orden_de_compra', 'empleado']

@admin.register(OrdenDeCompraProducto)
class OrdenDeCompraProductoAdmin(admin.ModelAdmin):
    list_display = ['orden_de_compra', 'producto']

@admin.register(OrdenDeCompraProveedor)
class OrdenDeCompraProveedorAdmin(admin.ModelAdmin):
    list_display = ['orden_de_compra', 'proveedor']

@admin.register(ReservaCliente)
class ReservaClienteAdmin(admin.ModelAdmin):
    list_display = ['reserva', 'cliente']
