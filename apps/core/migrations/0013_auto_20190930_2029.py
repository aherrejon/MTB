# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20190926_2308'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suscription',
            old_name='package',
            new_name='package_type',
        ),
        migrations.AddField(
            model_name='suscription',
            name='package_status',
            field=models.CharField(default=b'U', max_length=1, verbose_name=b'Paquete Entregado', choices=[(b'D', b'Entregado'), (b'U', b'Pendiente')]),
        ),
        migrations.AlterField(
            model_name='suscription',
            name='payment',
            field=models.FileField(upload_to=b'payments/', null=True, verbose_name=b'Pago', blank=True),
        ),
    ]
