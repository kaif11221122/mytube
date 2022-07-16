from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class user_data(models.Model):
    username = models.ForeignKey(
        User, on_delete=models.CASCADE,
    )
    profile_image = models.CharField(max_length=50)
