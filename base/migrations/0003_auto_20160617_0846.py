# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 08:46
from __future__ import unicode_literals

import ckeditor.fields
import datetime
from django.db import migrations
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20160617_0807'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gttg',
            options={'verbose_name': 'GetToGether'},
        ),
        migrations.AddField(
            model_name='audience',
            name='content',
            field=ckeditor.fields.RichTextField(default=datetime.datetime(2016, 6, 17, 8, 46, 33, 110571, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
