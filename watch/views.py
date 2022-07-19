from django.http import HttpResponse
from django.shortcuts import render
from user_authentication.models import user_data
from channel.models import video_info
from django.db.models import F
# Create your views here.


def watch(request, id):
    all_videos_data = video_info.objects.all().exclude(id=id)
    video_data = video_info.objects.filter(id=id)
    video_data.update(video_views=F('video_views') + 1)
    print(video_data.values())
    context = {
        'all_videos_data': all_videos_data,
        'video_data': video_data[0],
    }
    if request.user.is_authenticated and not request.user.is_superuser:
        image = user_data.objects.filter(username_id=request.user.id)[0]
        context['image'] = image
        return render(request, 'watch/loggedin.html', context)
    else:
        return render(request, 'watch/non_loggedin.html', context)
