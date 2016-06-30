# -*- coding: utf-8 -*-
# pylint: disable=W0201,R0903,C0301,C0330,C0103

from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from base.models import Audience


class AudienceInlineAdmin(admin.TabularInline):
    model = Audience
    extra = 1


class AudienceAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(config_name='basic'))

    class Meta:
        model = Audience
        exclude = []


class AudienceAdmin(admin.ModelAdmin):
    form = AudienceAdminForm


admin.site.register(Audience, AudienceAdmin)
