# -*- coding: utf-8 -*-
# pylint: disable=R0903

from django.db import models
from ckeditor.fields import RichTextField


class Gttg(models.Model):
    title = models.CharField(max_length=40)
    subtitle = models.CharField(max_length=100)
    start_time = models.DateTimeField('start date')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'GetToGether'


class Intro(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(config_name='basic')
    gttg = models.ForeignKey(Gttg, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Topic(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(config_name='basic')
    gttg = models.ForeignKey(Gttg, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Audience(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(config_name='basic')
    gttg = models.ForeignKey(Gttg, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
