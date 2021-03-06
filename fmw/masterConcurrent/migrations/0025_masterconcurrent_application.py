# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-14 16:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
        ('masterConcurrent', '0024_auto_20180214_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterconcurrent',
            name='application',
            field=models.ForeignKey(db_column='application_id', default=1, on_delete=django.db.models.deletion.PROTECT, related_name='concurrent_application', to='applications.TsApplications'),
            preserve_default=False,
        ),
    ]
