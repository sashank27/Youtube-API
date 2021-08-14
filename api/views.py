from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, filters
from .serializers import VideoSerializer
from .models import Video


class VideoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows video list to be viewed
    """
    queryset = Video.objects.all().order_by('-create_time')
    serializer_class = VideoSerializer

    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]

    search_fields = ['title', 'description']            # Apply pattern match search for title and description field
    filterset_fields = ['channel_title']                # Exact match fetching for channel title
    ordering_fields = ['create_time', 'publish_time']   # Allow ordering based on publish time and creation time
