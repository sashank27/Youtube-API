from django.db import models

class Video(models.Model):

    # video and channel ID
    video_id = models.CharField(max_length=100)
    channel_id = models.CharField(max_length=100)

    # Text Entries related to particular video
    title = models.CharField(null=True, blank=True, max_length=500)
    description = models.TextField(null=True, blank=True)
    channel_title = models.CharField(null=True, blank=True, max_length=500)

    # Timestamp entries for a video
    publish_time = models.DateTimeField()
    create_time = models.DateTimeField(auto_now_add=True)
