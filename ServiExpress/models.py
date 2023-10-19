from django.db import models

class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=100)

class Empleado(models.Model):
    id_empleado = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cargo = models.CharField(max_length=20)
    estado = models.DecimalField(max_digits=10, decimal_places=0)

class Factura(models.Model):
    id_factura = models.IntegerField(primary_key=True)
    id_reserva = models.IntegerField()
    fecha = models.DateField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

class OrdenDeCompra(models.Model):
    id_orden_de_pedido = models.IntegerField(primary_key=True)
    id_proveedor = models.IntegerField()
    id_producto = models.IntegerField()
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    empleado = models.IntegerField()
    comentario = models.TextField()  # Reemplace 'unknown' por TextField

class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class Proveedor(models.Model):
    id_proveedor = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    contacto = models.CharField(max_length=50)
    rubro = models.CharField(max_length=20)

class Reserva(models.Model):
    id_reserva = models.IntegerField(primary_key=True)
    id_cliente = models.IntegerField()
    fecha = models.DateField()
    hora = models.CharField(max_length=255)  # Reemplace 'unknown' por un campo de texto adecuado
    servicio = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class Servicio(models.Model):
    id_servicio = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class FacturaReserva(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)

class OrdenDeCompraEmpleado(models.Model):
    orden_de_compra = models.ForeignKey(OrdenDeCompra, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

class OrdenDeCompraProducto(models.Model):
    orden_de_compra = models.ForeignKey(OrdenDeCompra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

class OrdenDeCompraProveedor(models.Model):
    orden_de_compra = models.ForeignKey(OrdenDeCompra, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

class ReservaCliente(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
