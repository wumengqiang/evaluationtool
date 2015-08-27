# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage', '0005_auto_20150825_0330'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Client_eva_PM',
            new_name='Client_eva',
        ),
        migrations.RenameModel(
            old_name='Freelancer_eva_PM',
            new_name='Freelancer_eva',
        ),
    ]
