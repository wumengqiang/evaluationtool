# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage', '0004_auto_20150825_0225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client_eva_pm',
            name='pmname',
        ),
        migrations.RemoveField(
            model_name='freelancer_eva_pm',
            name='pmname',
        ),
    ]
