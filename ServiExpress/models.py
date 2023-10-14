from django.db import models

# Definición de la tabla Cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=100)
    estado = models.CharField(max_length=20)

# Definición de la tabla Servicio
class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

# Definición de la tabla Reserva
class Reserva(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)    

# Definición de la tabla Proveedor
class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    contacto = models.CharField(max_length=50)
    rubro = models.CharField(max_length=20)

# Definición de la tabla Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

# Definición de la tabla Factura
class Factura(models.Model):
    id_reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

# Definición de la tabla Empleado
class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cargo = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)

# Definición de la tabla Orden_de_pedido
class OrdenDePedido(models.Model):
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)



# Agregar el campo 'servicio' a la tabla Reserva
Reserva.add_to_class('servicio', models.ForeignKey(Servicio, on_delete=models.CASCADE))

# Agregar el campo 'empleado' a la tabla Orden_de_pedido
OrdenDePedido.add_to_class('empleado', models.ForeignKey(Empleado, on_delete=models.CASCADE))
