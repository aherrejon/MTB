# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20170608_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cyclist',
            name='nickname',
            field=models.CharField(db_index=True, max_length=50, null=True, verbose_name=b'Apodo', blank=True),
        ),
    ]
