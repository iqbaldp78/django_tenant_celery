# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-14 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concurrentManager', '0031_auto_20180214_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='concurrentlist',
            name='param_value_meaning',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]