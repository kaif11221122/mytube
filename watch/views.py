from django.http import HttpResponse
from django.shortcuts import render
from channel.models import video_info
# Create your views here.


def watch(request, id):
    all_videos_data = video_info.objects.all().exclude(id=id)
    for i in all_videos_data:
        print(type(i))
        print(i,'\n\n')
        
    video_data = video_info.objects.filter(id=id)
    context = {
        'all_videos_data': all_videos_data,
        'video_data': video_data[0],
    }
    return render(request, 'watch/index.html', context)
