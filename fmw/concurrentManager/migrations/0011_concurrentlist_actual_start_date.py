# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-08 06:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concurrentManager', '0010_auto_20180104_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='concurrentlist',
            name='actual_start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
