# Generated by Django 4.0.4 on 2022-06-01 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_persona_personas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personas',
            name='rut',
            field=models.PositiveBigIntegerField(primary_key=True, serialize=False, verbose_name='Rut'),
        ),
    ]
