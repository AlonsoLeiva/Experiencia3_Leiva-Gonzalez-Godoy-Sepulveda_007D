# Generated by Django 4.0.4 on 2022-06-01 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Civil',
            fields=[
                ('idCivil', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de estado civil')),
                ('nombreCivil', models.CharField(max_length=50, verbose_name='Nombre estado civil')),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('idgenero', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id género')),
                ('NombreGenero', models.CharField(max_length=50, verbose_name='Nombre Género')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('idregion', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Region')),
                ('NombreRegion', models.CharField(max_length=50, verbose_name='Nombre Region')),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('nombre', models.CharField(max_length=100, verbose_name='Nombres')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('rut', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Rut')),
                ('email', models.CharField(max_length=200, verbose_name='Email')),
                ('contraseña', models.CharField(max_length=100, verbose_name='Contraseña')),
                ('conficontraseña', models.CharField(max_length=100, verbose_name='Confirmar Contraseña')),
                ('direccion', models.CharField(max_length=100, verbose_name='Dirección')),
                ('civil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.civil')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.genero')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.region')),
            ],
        ),
    ]
