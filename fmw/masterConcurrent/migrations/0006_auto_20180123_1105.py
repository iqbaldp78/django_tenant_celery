# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-23 04:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterConcurrent', '0005_masterconcurrentdetail_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterconcurrent',
            name='concurrent_type',
            field=models.IntegerField(max_length=255),
        ),
        migrations.AlterField(
            model_name='masterconcurrentdetail',
            name='type',
            field=models.IntegerField(blank=True, max_length=255),
        ),
    ]
