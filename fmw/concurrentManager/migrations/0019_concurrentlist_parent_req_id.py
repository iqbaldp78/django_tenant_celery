# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-29 04:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concurrentManager', '0018_auto_20180129_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='concurrentlist',
            name='parent_req_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]