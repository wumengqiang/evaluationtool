# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage', '0002_auto_20150824_0615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_eva_pm',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='freelancer_eva_pm',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
