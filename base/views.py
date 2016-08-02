# -*- coding: utf-8 -*-
# pylint: disable=E1101

# from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import viewsets
from rest_framework import response, schemas
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from base.models import Gttg, Intro, Topic, Audience
from base.serializers import GttgSerializer, IntroSerializer, TopicSerializer, AudienceSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@api_view()
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='GTTG API')
    return response.Response(generator.get_schema(request=request))


class GttgViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Gttg.objects.all()
    serializer_class = GttgSerializer


class IntroViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Intro.objects.all()
    serializer_class = IntroSerializer


class TopicViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class AudienceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Audience.objects.all()
    serializer_class = AudienceSerializer
