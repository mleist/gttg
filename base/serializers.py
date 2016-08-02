# -*- coding: utf-8 -*-
# pylint: disable=R0903

from rest_framework import serializers
from base.models import Gttg, Intro, Topic, Audience


class GttgSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Gttg
        fields = ('pk', 'url', 'title', 'subtitle', 'start_time')


class IntroSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Intro
        fields = ('pk', 'url', 'title', 'content', 'gttg')


class TopicSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Topic
        fields = ('pk', 'url', 'title', 'content', 'gttg')


class AudienceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Audience
        fields = ('pk', 'url', 'title', 'content', 'gttg')
