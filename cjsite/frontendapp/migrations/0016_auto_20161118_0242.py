# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 02:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontendapp', '0015_auto_20161117_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='field',
        ),
        migrations.RemoveField(
            model_name='course_college_map',
            name='college',
        ),
        migrations.RemoveField(
            model_name='course_college_map',
            name='course',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Course_College_Map',
        ),
        migrations.DeleteModel(
            name='Field',
        ),
    ]
