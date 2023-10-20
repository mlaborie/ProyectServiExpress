from django.contrib import admin

from .models import Cliente, Empleado, Factura, OrdenDeCompra, Producto, Proveedor, Servicio, Reserva, FacturaReserva, OrdenDeCompraEmpleado, OrdenDeCompraProducto, OrdenDeCompraProveedor, ReservaCliente, CustomUser

admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Factura)
admin.site.register(OrdenDeCompra)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Servicio)
admin.site.register(Reserva)
admin.site.register(FacturaReserva)
admin.site.register(OrdenDeCompraEmpleado)
admin.site.register(OrdenDeCompraProducto)
admin.site.register(OrdenDeCompraProveedor)
admin.site.register(ReservaCliente)
admin.site.register(CustomUser)
