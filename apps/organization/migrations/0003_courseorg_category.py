# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-01-23 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='category',
            field=models.CharField(choices=[('personal', '个人'), ('agency', '教育机构'), ('shool', '高校')], default='agency', max_length=20, verbose_name='机构类别'),
        ),
    ]
