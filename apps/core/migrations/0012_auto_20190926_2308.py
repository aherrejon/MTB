# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20190925_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='suscription',
            name='payment',
            field=models.FileField(null=True, upload_to=b'payments/', blank=True),
        ),
        migrations.AlterField(
            model_name='suscription',
            name='size',
            field=models.CharField(default=b'N', max_length=3, verbose_name=b'Talla', choices=[(b'N', b'N'), (b'S', b'S'), (b'M', b'M'), (b'L', b'L'), (b'XL', b'XL'), (b'2XL', b'2XL'), (b'3XL', b'3XL'), (b'4XL', b'4XL')]),
        ),
    ]
