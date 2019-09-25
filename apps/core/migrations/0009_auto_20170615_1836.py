# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20170615_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suscription',
            name='cyclist',
            field=models.ForeignKey(verbose_name=b'Ciclista', to='core.Cyclist', null=True),
        ),
        migrations.AlterField(
            model_name='suscription',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
