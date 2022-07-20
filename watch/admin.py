from dis import dis
from django.contrib import admin
from .models import likes, dislikes, comments
# Register your models here.
admin.site.register(likes)
admin.site.register(dislikes)
admin.site.register(comments)