from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.db import models
from cloudinary.models import CloudinaryField

# class user_data(models.Model):
#   image = CloudinaryField('profile_image')


class user_data(models.Model):
    username = models.ForeignKey(
        User, on_delete=models.CASCADE,
    )
    profile_image = CloudinaryField('image')
