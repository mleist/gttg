# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 10:28
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20160617_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', ckeditor.fields.RichTextField()),
                ('gttg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Gttg')),
            ],
        ),
    ]