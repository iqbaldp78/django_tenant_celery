# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-31 06:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('concurrentManager', '0025_auto_20180130_1644'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='concurrentlist',
            options={'ordering': ['-id']},
        ),
    ]
