# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontendapp', '0023_college_activity_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='visit_count',
            field=models.IntegerField(default=0),
        ),
    ]
