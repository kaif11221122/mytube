from django.shortcuts import render
from user_authentication.models import user_data
from channel.models import video_info
from django.db.models import F
from django.contrib.auth.models import User
from watch.models import likes, dislikes, comments
# Create your views here.


def watch(request, id):

    # video_comments = comments.objects.filter(
    #     video_id=id).select_related('user_id')
    # print(video_comments[0], type(video_comments[0]))
    # print(getattr(video_comments[0], 'user_id'))
    # print(request.user.id)

    video_comments = comments.objects.filter(video_id=id).select_related('user_id')
    # print('\n\n\n')
    # for i in video_comments:
    #     print(i)
    # print('\n\n\n')
    # print(getattr(video_comments[0], 'user_id'))

    print('\n\n')
    print(str(video_comments.query))

    all_videos_data = video_info.objects.all().exclude(id=id)
    video_data = video_info.objects.filter(id=id)
    video_data.update(video_views=F('video_views') + 1)
    video_id = video_data[0].id

    current_likes_count = len(likes.objects.filter(
        video_id=video_id).distinct('user_id'))
    current_dislikes_count = len(dislikes.objects.filter(
        video_id=video_id).distinct('user_id'))

    context = {
        'all_videos_data': all_videos_data,
        'video_data': video_data[0],
        'likes_count': current_likes_count,
        'dislikes_count': current_dislikes_count,
        'video_comments': video_comments,
    }
    if request.user.is_authenticated and not request.user.is_superuser:
        image = user_data.objects.filter(username_id=request.user.id)[0]
        context['image'] = image
        return render(request, 'watch/loggedin.html', context)
    else:
        return render(request, 'watch/non_loggedin.html', context)
