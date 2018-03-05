# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-01-20 13:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='教师名字')),
                ('job_years', models.IntegerField(default=0, verbose_name='工作年限')),
                ('position', models.CharField(max_length=50, verbose_name='工作职位')),
                ('company', models.CharField(max_length=50, verbose_name='就职公司')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('feature', models.CharField(max_length=30, verbose_name='教学特点')),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg', verbose_name='教育机构')),
            ],
            options={
                'verbose_name_plural': '教师',
                'verbose_name': '教师',
            },
        ),
    ]
