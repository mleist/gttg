# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 13:45
from __future__ import unicode_literals

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    replaces = [('base', '0001_initial'), ('base', '0002_auto_20160617_0807'), ('base', '0003_auto_20160617_0846'), ('base', '0004_auto_20160617_0948'), ('base', '0005_intro'), ('base', '0006_auto_20160621_1214'), ('base', '0007_auto_20160621_1241')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Gttg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='start date')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('gttg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Gttg')),
                ('content', ckeditor.fields.RichTextField(default=datetime.datetime(2016, 6, 17, 9, 48, 36, 293162, tzinfo=utc))),
            ],
        ),
        migrations.AddField(
            model_name='audience',
            name='gttg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Gttg'),
        ),
        migrations.AlterModelOptions(
            name='gttg',
            options={'verbose_name': 'dfsfd'},
        ),
        migrations.AddField(
            model_name='gttg',
            name='title',
            field=models.CharField(default=datetime.datetime(2016, 6, 17, 8, 7, 7, 140882, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
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
        migrations.CreateModel(
            name='Intro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', ckeditor.fields.RichTextField()),
                ('gttg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Gttg')),
            ],
        ),
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
        migrations.AlterField(
            model_name='gttg',
            name='title',
            field=models.CharField(max_length=40),
        ),
    ]
