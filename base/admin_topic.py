# -*- coding: utf-8 -*-
# pylint: disable=R0903

from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from base.models import Topic


class TopicInlineAdmin(admin.TabularInline):
    model = Topic
    extra = 1


class TopicAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(config_name='basic'))

    class Meta:
        model = Topic
        exclude = []


class TopicAdmin(admin.ModelAdmin):
    form = TopicAdminForm


admin.site.register(Topic, TopicAdmin)
