# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qaa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='q_id',
            field=models.CharField(max_length=50),
        ),
    ]
