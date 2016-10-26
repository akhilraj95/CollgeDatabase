# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontendapp', '0007_college_model_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='brief',
            field=models.CharField(default=b'We are working on the brief.', max_length=150),
        ),
        migrations.AlterField(
            model_name='college',
            name='model_pic',
            field=models.ImageField(default=b'media/not_available.png', null=True, upload_to=b'media/'),
        ),
    ]
