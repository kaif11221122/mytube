from django.db import models
from django.forms import CharField, IntegerField
from cloudinary.models import CloudinaryField
# Create your models here.


class video(models.Model):
    thumbnail = CloudinaryField('Image')
    title = models.CharField(max_length=50)
    channel = models.CharField(max_length=20)
    video_views = models.IntegerField(null=True, default=0)
