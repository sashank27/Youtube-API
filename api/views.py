from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import VideoSerializer
from .models import Video


class VideoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows video list to be viewed
    """
    queryset = Video.objects.all().order_by('-create_time')
    serializer_class = VideoSerializer
