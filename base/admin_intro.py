# -*- coding: utf-8 -*-
# pylint: disable=W0201,R0903,C0301,C0330,C0103

from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget


from base.models import Intro


class IntroInlineAdmin(admin.TabularInline):
    model = Intro
    extra = 1


class IntroAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(config_name='basic'))

    class Meta:
        model = Intro
        exclude = []


class IntroAdmin(admin.ModelAdmin):
    form = IntroAdminForm


admin.site.register(Intro, IntroAdmin)
