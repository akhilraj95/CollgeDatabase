# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-22 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontendapp', '0028_auto_20170122_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='field',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='professor',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
