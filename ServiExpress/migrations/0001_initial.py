# Generated by Django 4.2.6 on 2023-11-25 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_empleado', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=20)),
                ('estado', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id_factura', models.AutoField(primary_key=True, serialize=False)),
                ('id_reserva', models.IntegerField()),
                ('fecha', models.DateField()),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('iva', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='OrdenDeCompra',
            fields=[
                ('id_orden_de_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('id_proveedor', models.IntegerField()),
                ('id_producto', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('empleado', models.IntegerField()),
                ('comentario', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.AutoField(primary_key=True, serialize=False)),
                ('razonSocial', models.CharField(max_length=50)),
                ('rut', models.CharField(max_length=50)),
                ('rubro', models.CharField(max_length=50)),
                ('contacto', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id_reserva', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('hora', models.CharField(max_length=255)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ServiExpress.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id_servicio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='ReservaCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ServiExpress.cliente')),
                ('reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ServiExpress.reserva')),
            ],
        ),
        migrations.AddField(
            model_name='reserva',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ServiExpress.servicio'),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ServiExpress.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenDeCompraProveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden_de_compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ServiExpress.ordendecompra')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ServiExpress.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenDeCompraProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden_de_compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ServiExpress.ordendecompra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ServiExpress.producto')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenDeCompraEmpleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ServiExpress.empleado')),
                ('orden_de_compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ServiExpress.ordendecompra')),
            ],
        ),
        migrations.CreateModel(
            name='FacturaReserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ServiExpress.factura')),
                ('reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ServiExpress.reserva')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, related_name='customuser_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='customuser_set', to='auth.permission')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
