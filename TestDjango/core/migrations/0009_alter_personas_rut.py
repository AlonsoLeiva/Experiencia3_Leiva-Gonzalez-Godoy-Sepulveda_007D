# Generated by Django 4.0.4 on 2022-06-01 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_personas_rut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personas',
            name='rut',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Rut'),
        ),
    ]
