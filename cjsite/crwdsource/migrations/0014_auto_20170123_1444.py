# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-23 14:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crwdsource', '0013_auto_20170122_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='access_ticket',
            name='acs_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date created'),
        ),
        migrations.AlterField(
            model_name='access_ticket',
            name='hash_key',
            field=models.CharField(default=b'76cfc10795ad28a6f9b740b695993c', max_length=30, unique=True),
        ),
    ]
