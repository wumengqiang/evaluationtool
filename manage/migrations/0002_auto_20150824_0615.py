# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Freelancer_eva_PM',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('pmname', models.CharField(max_length=30)),
                ('projectname', models.CharField(max_length=50)),
                ('eva_reqquirement', models.IntegerField()),
                ('eva_management', models.IntegerField()),
                ('eva_communication', models.IntegerField()),
                ('eva_content', models.CharField(max_length=1000)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='EvaluationForPM',
            new_name='Client_eva_PM',
        ),
    ]
