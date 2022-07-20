from django.db import models
from django.contrib.auth.models import User
from channel.models import video_info
# Create your models here.

class likes(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE,
    )
    video_id = models.ForeignKey(
        video_info, on_delete=models.CASCADE,
    )

class dislikes(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE,
    )
    video_id = models.ForeignKey(
        video_info, on_delete=models.CASCADE,
    )