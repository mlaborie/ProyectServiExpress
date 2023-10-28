from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission


class Cliente(models.Model):
    rut = models.CharField(max_length=50,primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.rut} {self.nombre} {self.apellido}"

class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cargo = models.CharField(max_length=20)
    estado = models.DecimalField(max_digits=10, decimal_places=0)

class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    id_reserva = models.IntegerField()
    fecha = models.DateField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

class OrdenDeCompra(models.Model):
    id_orden_de_pedido = models.AutoField(primary_key=True)
    id_proveedor = models.IntegerField()
    id_producto = models.IntegerField()
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    empleado = models.IntegerField()
    comentario = models.TextField()  

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    razonSocial = models.CharField(max_length=50)
    rut = models.CharField(max_length=50)
    rubro = models.CharField(max_length=50)
    contacto = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    
class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.nombre} {self.precio} "

class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.CharField(max_length=255)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)


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

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El Email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Los superusuarios deben tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Los superusuarios deben tener is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    groups = models.ManyToManyField('auth.Group', related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='customuser_set', blank=True)

    def __str__(self):
        return self.username
