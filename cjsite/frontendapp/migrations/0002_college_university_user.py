# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontendapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=40)),
                ('date_founded', models.DateField(verbose_name=b'date founded')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_founded', models.DateField(verbose_name=b'date founded')),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=30)),
                ('reg_date', models.DateTimeField(auto_now=True, verbose_name=b'date registered')),
                ('bdate', models.DateTimeField(verbose_name=b'bdate')),
                ('location', models.CharField(max_length=30)),
                ('field', models.CharField(max_length=30)),
            ],
        ),
    ]
