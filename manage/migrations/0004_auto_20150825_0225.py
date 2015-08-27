# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage', '0003_auto_20150824_0621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='freelancer_eva_pm',
            old_name='eva_reqquirement',
            new_name='eva_requirement',
        ),
    ]
