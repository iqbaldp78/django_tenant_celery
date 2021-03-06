# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-30 10:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('masterConcurrent', '0015_remove_masterconcurrentdetail_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='masterconcurrent',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='masterconcurrent',
            name='last_update_by',
        ),
        migrations.RemoveField(
            model_name='masterconcurrentdetail',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='masterconcurrentdetail',
            name='last_update_by',
        ),
        migrations.AddField(
            model_name='masterconcurrent',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='masterconcurrent',
            name='last_updated_by',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='masterconcurrent',
            name='login_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='masterconcurrentdetail',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='masterconcurrentdetail',
            name='last_updated_by',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='masterconcurrentdetail',
            name='login_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='masterconcurrent',
            name='created_by',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='masterconcurrent',
            name='last_update_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='masterconcurrentdetail',
            name='created_by',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='masterconcurrentdetail',
            name='last_update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
