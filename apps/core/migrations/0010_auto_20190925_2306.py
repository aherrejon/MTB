# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20170615_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='cyclist',
            name='city',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Ciudad', blank=True),
        ),
        migrations.AddField(
            model_name='suscription',
            name='account',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Cuenta', blank=True),
        ),
        migrations.AddField(
            model_name='suscription',
            name='comments',
            field=models.CharField(max_length=250, null=True, verbose_name=b'Observaciones', blank=True),
        ),
        migrations.AddField(
            model_name='suscription',
            name='comments2',
            field=models.CharField(max_length=250, null=True, verbose_name=b'Observaciones2', blank=True),
        ),
        migrations.AddField(
            model_name='suscription',
            name='distance',
            field=models.CharField(default=b'50', max_length=3, verbose_name=b'Distancia', choices=[(b'35', b'35'), (b'50', b'50'), (b'65', b'65')]),
        ),
        migrations.AddField(
            model_name='suscription',
            name='logo',
            field=models.BooleanField(default=False, verbose_name=b'Logo'),
        ),
        migrations.AddField(
            model_name='suscription',
            name='paid_date',
            field=models.DateField(null=True, verbose_name=b'Fecha Deposito', blank=True),
        ),
        migrations.AddField(
            model_name='suscription',
            name='sex',
            field=models.CharField(default=b'M', max_length=1, verbose_name=b'Sexo', choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
        migrations.AlterField(
            model_name='cyclist',
            name='age',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Edad', blank=True),
        ),
        migrations.AlterField(
            model_name='cyclist',
            name='birthday',
            field=models.DateField(null=True, verbose_name=b'Fecha Nacimiento', blank=True),
        ),
        migrations.AlterField(
            model_name='cyclist',
            name='blood',
            field=models.CharField(default=b'', max_length=7, null=True, verbose_name=b'Tipo Sangre', blank=True),
        ),
        migrations.AlterField(
            model_name='cyclist',
            name='category',
            field=models.CharField(default=b'P', max_length=1, verbose_name=b'Clasificaci\xc3\xb3n', blank=True, choices=[(b'P', b'Principiante'), (b'I', b'Intermedia'), (b'A', b'Avanzada')]),
        ),
        migrations.AlterField(
            model_name='cyclist',
            name='club',
            field=models.CharField(db_index=True, max_length=50, null=True, verbose_name=b'Club', blank=True),
        ),
        migrations.AlterField(
            model_name='cyclist',
            name='contact_name',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Nombre Contacto', blank=True),
        ),
        migrations.AlterField(
            model_name='cyclist',
            name='contact_phone',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Telefono Contacto', blank=True),
        ),
        migrations.AlterField(
            model_name='cyclist',
            name='emergency_phone',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Telefono Emergencia', blank=True),
        ),
        migrations.AlterField(
            model_name='cyclist',
            name='phone',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Telefono', blank=True),
        ),
        migrations.AlterField(
            model_name='cyclist',
            name='secondlastname',
            field=models.CharField(db_index=True, max_length=50, verbose_name=b'Apellido2', blank=True),
        ),
        migrations.AlterField(
            model_name='suscription',
            name='package',
            field=models.CharField(default=b'1', max_length=1, verbose_name=b'Paquete', choices=[(b'1', b'Paquete 1'), (b'2', b'Paquete 2')]),
        ),
        migrations.AlterField(
            model_name='suscription',
            name='size',
            field=models.CharField(default=b'N', max_length=3, verbose_name=b'Talla', choices=[(b'N', b'None'), (b'S', b'Small'), (b'M', b'Medium'), (b'L', b'Large'), (b'XL', b'Extra Large'), (b'XXL', b'Doble Extra Large')]),
        ),
        migrations.AlterField(
            model_name='suscription',
            name='status',
            field=models.CharField(default=b'P', max_length=1, verbose_name=b'Estado Inscripcion', choices=[(b'A', b'Aceptado'), (b'P', b'En Proceso')]),
        ),
    ]
