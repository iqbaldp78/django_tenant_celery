# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-24 10:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lookups', '0005_auto_20171208_1500'),
        ('masterConcurrent', '0013_auto_20180124_1056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='masterconcurrentdetail',
            name='concurrent_lookup_type_id',
        ),
        migrations.AddField(
            model_name='masterconcurrentdetail',
            name='concurrent_lookup_detail_type_id',
            field=models.ForeignKey(db_column='concurrent_lookup_detail_type_id', default=1, on_delete=django.db.models.deletion.CASCADE, related_name='lookup_detail_conc', to='lookups.TsLookupCodes'),
        ),
    ]