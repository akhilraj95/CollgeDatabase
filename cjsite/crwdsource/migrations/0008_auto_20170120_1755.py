# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crwdsource', '0007_auto_20170120_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='access_ticket',
            name='hash_key',
            field=models.CharField(default=b'2d956163829574a6fd332970b38144', max_length=30, unique=True),
        ),
    ]