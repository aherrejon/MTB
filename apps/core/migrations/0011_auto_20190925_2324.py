# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20190925_2306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suscription',
            name='sex',
        ),
        migrations.AddField(
            model_name='cyclist',
            name='sex',
            field=models.CharField(default=b'M', max_length=1, verbose_name=b'Sexo', choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
    ]
