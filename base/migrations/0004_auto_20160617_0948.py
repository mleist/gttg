# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 09:48
from __future__ import unicode_literals

import ckeditor.fields
import datetime
from django.db import migrations
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20160617_0846'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Para',
        ),
        migrations.AddField(
            model_name='topic',
            name='content',
            field=ckeditor.fields.RichTextField(default=datetime.datetime(2016, 6, 17, 9, 48, 36, 293162, tzinfo=utc)),
            preserve_default=False,
        ),
    ]