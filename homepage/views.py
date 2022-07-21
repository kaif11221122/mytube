from django.shortcuts import render
from user_authentication.models import user_data
from channel.models import video_info
# Create your views here.


def homepage(request):
    videos_data = video_info.objects.all().values()
    if request.user.is_authenticated and not request.user.is_superuser:
        image = user_data.objects.filter(username_id=request.user.id)[0]
        print('\n\n\n')
        print(image)
        print('\n\n\n')
        context = {
            'image': image,
            'videos_data': videos_data,
        }
        return render(request, 'homepage/loggedin.html', context)
    else:
        context = {
            'videos_data': videos_data
        }
        return render(request, 'homepage/non_loggedin.html', context)
