# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170607_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='cyclist',
            name='blood',
            field=models.CharField(default=b'', max_length=7),
        ),
        migrations.AddField(
            model_name='suscription',
            name='supply',
            field=models.CharField(default=b'N', max_length=1, choices=[(b'N', b'Nada'), (b'B', b'Frijol'), (b'R', b'Arroz'), (b'D', b'Despensa'), (b'O', b'Otro')]),
        ),
        migrations.AlterField(
            model_name='suscription',
            name='size',
            field=models.CharField(default=b'N', max_length=3, choices=[(b'N', b'None'), (b'S', b'S'), (b'M', b'M'), (b'L', b'L'), (b'XL', b'XL'), (b'XXL', b'XXL')]),
        ),
        migrations.AlterField(
            model_name='suscription',
            name='status',
            field=models.CharField(default=b'U', max_length=1, choices=[(b'A', b'Aceptado'), (b'P', b'En Proceso')]),
        ),
    ]
