# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 06:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontendapp', '0024_courses_visit_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('field', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='college',
            name='Placement_majorcompany1',
            field=models.CharField(default=b'None', max_length=150),
        ),
        migrations.AddField(
            model_name='college',
            name='association',
            field=models.CharField(default=b'None', max_length=1000),
        ),
        migrations.AddField(
            model_name='college',
            name='clubs',
            field=models.CharField(default=b'No Data available', max_length=2000),
        ),
        migrations.AddField(
            model_name='college',
            name='mode_of_operation',
            field=models.CharField(choices=[(b'a', b'Private'), (b'b', b'Government'), (b'c', b'Government Aided'), (b'd', b'Trust')], default=b'a', max_length=1),
        ),
        migrations.AddField(
            model_name='college',
            name='other_text',
            field=models.CharField(default=b'no data', max_length=3000),
        ),
        migrations.AddField(
            model_name='college',
            name='placement_majorcompany10',
            field=models.CharField(default=b'None', max_length=150),
        ),
        migrations.AddField(
            model_name='college',
            name='placement_majorcompany2',
            field=models.CharField(default=b'None', max_length=150),
        ),
        migrations.AddField(
            model_name='college',
            name='placement_majorcompany3',
            field=models.CharField(default=b'None', max_length=150),
        ),
        migrations.AddField(
            model_name='college',
            name='placement_majorcompany4',
            field=models.CharField(default=b'None', max_length=150),
        ),
        migrations.AddField(
            model_name='college',
            name='placement_majorcompany5',
            field=models.CharField(default=b'None', max_length=150),
        ),
        migrations.AddField(
            model_name='college',
            name='placement_majorcompany6',
            field=models.CharField(default=b'None', max_length=150),
        ),
        migrations.AddField(
            model_name='college',
            name='placement_majorcompany7',
            field=models.CharField(default=b'None', max_length=150),
        ),
        migrations.AddField(
            model_name='college',
            name='placement_majorcompany8',
            field=models.CharField(default=b'None', max_length=150),
        ),
        migrations.AddField(
            model_name='college',
            name='placement_majorcompany9',
            field=models.CharField(default=b'None', max_length=150),
        ),
        migrations.AddField(
            model_name='college',
            name='placement_num_eligible',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='college',
            name='placement_num_placed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='college',
            name='placement_num_with_two_offers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='college',
            name='recognition',
            field=models.CharField(default=b'None', max_length=1000),
        ),
        migrations.AddField(
            model_name='college',
            name='special_achievement',
            field=models.CharField(default=b'None', max_length=150),
        ),
        migrations.AddField(
            model_name='college',
            name='student_strength',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='courses',
            name='is_post_graduate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='professor',
            name='college',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='frontendapp.College'),
        ),
    ]
