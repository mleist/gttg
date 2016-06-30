# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 12:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='gttg',
            name='subtitle',
            field=models.CharField(default=datetime.datetime(2016, 6, 21, 12, 14, 43, 119267, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gttg',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
