# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluationForPM',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('pmname', models.CharField(max_length=30)),
                ('projectname', models.CharField(max_length=50)),
                ('eva_progress', models.IntegerField()),
                ('eva_quality', models.IntegerField()),
                ('eva_service', models.IntegerField()),
                ('eva_content', models.CharField(max_length=1000)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
