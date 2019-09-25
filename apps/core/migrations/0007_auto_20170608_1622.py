# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20170608_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cyclist',
            name='age',
            field=models.PositiveIntegerField(verbose_name=b'Edad'),
        ),
        migrations.AlterField(
            model_name='cyclist',
            name='birthday',
            field=models.DateField(verbose_name=b'Fecha Nacimiento'),
        ),
        migrations.AlterField(
            model_name='cyclist',
            name='blood',
            field=models.CharField(default=b'', max_length=7, verbose_name=b'Tipo Sangre'),
        ),
        migrations.AlterField(
            model_name='cyclist',
            name='category',
            field=models.CharField(default=b'P', max_length=1, verbose_name=b'Clasificaci\xc3\xb3n', choices=[(b'P', b'Principiante'), (b'I', b'Intermedia'), (b'A', b'Avanzada')]),
        ),
        migrations.AlterField(
            model_name='cyclist',
            name='club',
            field=models.CharField(max_length=50, verbose_name=b'Club', db_index=True),
        ),
        migrations.AlterField(
            model_name='cyclist',
            name='contact_name',
            field=models.CharField(max_length=50, verbose_name=b'Nombre Contacto'),
        ),
        migrations.AlterField(
            model_name='cyclist',
            name='contact_phone',
            field=models.CharField(max_length=50, verbose_name=b'Telefono Contacto'),
        ),
        migrations.AlterField(
            model_name='cyclist',
            name='email',
            field=models.EmailField(max_length=254, verbose_name=b'Email', db_index=True),
        ),
        migrations.AlterField(
            model_name='cyclist',
            name='emergency_phone',
            field=models.CharField(max_length=50, verbose_name=b'Telefono Emergencia'),
        ),
        migrations.AlterField(
            model_name='cyclist',
            name='firstname',
            field=models.CharField(max_length=50, verbose_name=b'Nombre', db_index=True),
        ),
        migrations.AlterField(
            model_name='cyclist',
            name='lastname',
            field=models.CharField(max_length=50, verbose_name=b'Apellido1', db_index=True),
        ),
        migrations.AlterField(
            model_name='cyclist',
            name='nickname',
            field=models.CharField(max_length=50, verbose_name=b'Apodo', db_index=True),
        ),
        migrations.AlterField(
            model_name='cyclist',
            name='phone',
            field=models.CharField(max_length=50, verbose_name=b'Telefono'),
        ),
        migrations.AlterField(
            model_name='cyclist',
            name='secondlastname',
            field=models.CharField(max_length=50, verbose_name=b'Apellido2', db_index=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(default=b'P', max_length=1, verbose_name=b'Categoria', choices=[(b'P', b'Principiante'), (b'I', b'Intermedia'), (b'A', b'Avanzada')]),
        ),
        migrations.AlterField(
            model_name='event',
            name='cost',
            field=models.DecimalField(verbose_name=b'Costo', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name=b'Fecha'),
        ),
        migrations.AlterField(
            model_name='event',
            name='distance',
            field=models.DecimalField(verbose_name=b'Distancia', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='event',
            name='jerseys',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Total Jerseys'),
        ),
        migrations.AlterField(
            model_name='event',
            name='left_jerseys',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Jerseys Disponibles'),
        ),
        migrations.AlterField(
            model_name='event',
            name='left_medals',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Medallas Disponibles'),
        ),
        migrations.AlterField(
            model_name='event',
            name='left_suscriptions',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Registros Disponibles'),
        ),
        migrations.AlterField(
            model_name='event',
            name='medals',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Total Medallas'),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=50, verbose_name=b'Nombre'),
        ),
        migrations.AlterField(
            model_name='event',
            name='suscriptions',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Total Registros'),
        ),
        migrations.AlterField(
            model_name='suscription',
            name='cyclist',
            field=models.ForeignKey(verbose_name=b'Ciclista', to='core.Cyclist'),
        ),
        migrations.AlterField(
            model_name='suscription',
            name='event',
            field=models.ForeignKey(verbose_name=b'Evento', to='core.Event'),
        ),
        migrations.AlterField(
            model_name='suscription',
            name='jersey',
            field=models.BooleanField(default=False, verbose_name=b'Jersey'),
        ),
        migrations.AlterField(
            model_name='suscription',
            name='medal',
            field=models.BooleanField(default=False, verbose_name=b'Medalla'),
        ),
        migrations.AlterField(
            model_name='suscription',
            name='number',
            field=models.PositiveIntegerField(verbose_name=b'Numero'),
        ),
        migrations.AlterField(
            model_name='suscription',
            name='package',
            field=models.CharField(default=b'U', max_length=1, verbose_name=b'Paquete Entregado', choices=[(b'D', b'Entregado'), (b'U', b'Pendiente')]),
        ),
        migrations.AlterField(
            model_name='suscription',
            name='ride',
            field=models.BooleanField(default=False, verbose_name=b'Transporte'),
        ),
        migrations.AlterField(
            model_name='suscription',
            name='size',
            field=models.CharField(default=b'N', max_length=3, verbose_name=b'Talla', choices=[(b'N', b'None'), (b'S', b'S'), (b'M', b'M'), (b'L', b'L'), (b'XL', b'XL'), (b'XXL', b'XXL')]),
        ),
        migrations.AlterField(
            model_name='suscription',
            name='status',
            field=models.CharField(default=b'U', max_length=1, verbose_name=b'Estado Inscripcion', choices=[(b'A', b'Aceptado'), (b'P', b'En Proceso')]),
        ),
        migrations.AlterField(
            model_name='suscription',
            name='supply',
            field=models.CharField(default=b'N', max_length=1, verbose_name=b'Kilo de Ayuda', choices=[(b'N', b'Nada'), (b'B', b'Frijol'), (b'R', b'Arroz'), (b'D', b'Despensa'), (b'O', b'Otro')]),
        ),
    ]
