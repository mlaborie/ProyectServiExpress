from django.contrib import admin

from .models import (
    Cliente,
    Empleado,
    Factura,
    OrdenDeCompra,
    Producto,
    Proveedor,
    Servicio,
    Reserva,
    FacturaReserva,
    OrdenDeCompraEmpleado,
    OrdenDeCompraProducto,
    OrdenDeCompraProveedor,
    ReservaCliente,
)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ("id_cliente", "nombre", "apellido", "correo", "telefono", "direccion")
    search_fields = ("nombre", "apellido", "correo")

admin.site.register(Cliente, ClienteAdmin)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ("id_empleado", "nombre", "apellido", "cargo", "estado")
    search_fields = ("nombre", "apellido", "cargo")

admin.site.register(Empleado, EmpleadoAdmin)

class FacturaAdmin(admin.ModelAdmin):
    list_display = ("id_factura", "id_reserva", "fecha", "subtotal", "iva", "total")
    search_fields = ("id_reserva", "fecha")

admin.site.register(Factura, FacturaAdmin)

class OrdenDeCompraAdmin(admin.ModelAdmin):
    list_display = ("id_orden_de_pedido", "id_proveedor", "id_producto", "cantidad", "precio", "empleado")
    search_fields = ("id_proveedor", "id_producto", "empleado")

admin.site.register(OrdenDeCompra, OrdenDeCompraAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id_producto", "nombre", "descripcion", "precio")
    search_fields = ("nombre", "descripcion")

admin.site.register(Producto, ProductoAdmin)

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ("id_proveedor", "nombre", "contacto", "rubro")
    search_fields = ("nombre", "contacto", "rubro")

admin.site.register(Proveedor, ProveedorAdmin)

class ServicioAdmin(admin.ModelAdmin):
    list_display = ("id_servicio", "nombre", "descripcion", "precio")
    search_fields = ("nombre", "descripcion")

admin.site.register(Servicio, ServicioAdmin)

class ReservaAdmin(admin.ModelAdmin):
    list_display = ("id_reserva", "cliente", "fecha", "hora", "servicio", "precio")
    search_fields = ("cliente", "fecha", "hora", "servicio")

admin.site.register(Reserva, ReservaAdmin)

class FacturaReservaAdmin(admin.ModelAdmin):
    list_display = ("factura", "reserva")
    search_fields = ("factura", "reserva")

admin.site.register(FacturaReserva, FacturaReservaAdmin)

class OrdenDeCompraEmpleadoAdmin(admin.ModelAdmin):
    list_display = ("orden_de_compra", "empleado")
    search_fields = ("orden_de_compra", "empleado")

admin.site.register(OrdenDeCompraEmpleado, OrdenDeCompraEmpleadoAdmin)

class OrdenDeCompraProductoAdmin(admin.ModelAdmin):
    list_display = ("orden_de_compra", "producto")
    search_fields = ("orden_de_compra", "producto")

admin.site.register(OrdenDeCompraProducto, OrdenDeCompraProductoAdmin)

class OrdenDeCompraProveedorAdmin(admin.ModelAdmin):
    list_display = ("orden_de_compra", "proveedor")
    search_fields = ("orden_de_compra", "proveedor")

admin.site.register(OrdenDeCompraProveedor, OrdenDeCompraProveedorAdmin)

class ReservaClienteAdmin(admin.ModelAdmin):
    list_display = ("reserva", "cliente")
    search_fields = ("reserva", "cliente")

admin.site.register(ReservaCliente, ReservaClienteAdmin)
