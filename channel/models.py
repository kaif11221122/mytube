from email.policy import default
from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class video_info(models.Model):
    thumbnail = CloudinaryField('Thumbnail')
    video_link = CloudinaryField('Video', resource_type="video")
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    channel_id = models.CharField(max_length=40, default=)
    video_views = models.IntegerField(null=True, default=0)
