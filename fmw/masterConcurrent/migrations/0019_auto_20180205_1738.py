# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-05 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterConcurrent', '0018_auto_20180205_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterconcurrentdetail',
            name='default_value',
            field=models.CharField(max_length=25, null=True),
        ),
    ]