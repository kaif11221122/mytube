from dataclasses import field
from django.forms import ModelForm
from .models import video


class video_creation_form(ModelForm):
    class Meta:
        model = video
        fields = '__all__'
