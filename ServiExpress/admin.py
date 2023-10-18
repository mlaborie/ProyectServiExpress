from django.contrib import admin
from .models import Cliente, Servicio, Reserva, Proveedor, Producto, Factura, Empleado, OrdenDePedido

admin.site.register(Cliente)
admin.site.register(Servicio)
admin.site.register(Reserva)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Factura)
admin.site.register(Empleado)
admin.site.register(OrdenDePedido)
