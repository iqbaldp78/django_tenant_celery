# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-30 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concurrentManager', '0024_auto_20180130_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concurrentlist',
            name='task_id',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True),
        ),
    ]
