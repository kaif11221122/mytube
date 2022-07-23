from django.forms import ModelForm
from .models import video_info


class video_creation_form(ModelForm):
    class Meta:
        model = video_info
        fields = [
            'thumbnail',
            'video_link',
            'title',
            'description',
            'channel_id',
        ]
