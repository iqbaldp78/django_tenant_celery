# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-14 11:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('concurrentManager', '0030_auto_20180214_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concurrentlist',
            name='concurrent_id',
            field=models.ForeignKey(db_column='concurrent_id', on_delete=django.db.models.deletion.DO_NOTHING, related_name='ts_concurrent_request', to='masterConcurrent.MasterConcurrent'),
        ),
    ]
