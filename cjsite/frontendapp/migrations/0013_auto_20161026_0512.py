# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 05:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontendapp', '0012_auto_20161025_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='alias',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='university',
            name='alias',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
