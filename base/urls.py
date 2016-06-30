# -*- coding: utf-8 -*-
# pylint: disable=C0103

from decouple import config

from django.conf.urls import url
from django.contrib import admin

from . import views

CFG_GTTG_TITLE = config('GTTG_TITLE', default='GTTG Administration', cast=str)


admin.site.site_title = CFG_GTTG_TITLE
admin.site.site_header = CFG_GTTG_TITLE


urlpatterns = [
    url(r'^$', views.index, name='index'),
]
