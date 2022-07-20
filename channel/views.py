from django.shortcuts import redirect, render
from .forms import video_creation_form
from django.http import HttpResponse, JsonResponse
from watch.models import likes, dislikes, comments
from .models import video_info
# Create your views here.


def like(request):
    if request.method == "GET":

        video_id = request.GET['video_id']

        current_likes_count = len(likes.objects.filter(
            video_id=video_id).distinct('user_id'))
        current_dislikes_count = len(dislikes.objects.filter(
            video_id=video_id).distinct('user_id'))

        if likes.objects.filter(user_id=request.user.id, video_id=video_id).exists():
            likes.objects.filter(user_id=request.user.id,
                                 video_id=video_id).delete()
            current_likes_count -= 1
        else:
            likes_obj = likes(
                user_id=request.user,
                video_id=video_info.objects.get(id=video_id),
            )
            likes_obj.save()
            if dislikes.objects.filter(user_id=request.user.id, video_id=video_id).exists():
                dislikes.objects.filter(
                    user_id=request.user.id, video_id=video_id).delete()
                current_dislikes_count -= 1
            current_likes_count += 1
        data = {
            "likes_count": int(current_likes_count),
            "dislikes_count": int(current_dislikes_count),
        }
        return JsonResponse(data)


def dislike(request):
    if request.method == "GET":

        video_id = request.GET['video_id']

        current_likes_count = len(likes.objects.filter(
            video_id=video_id).distinct('user_id'))
        current_dislikes_count = len(dislikes.objects.filter(
            video_id=video_id).distinct('user_id'))

        print(current_dislikes_count)
        if dislikes.objects.filter(user_id=request.user.id, video_id=video_id).exists():
            dislikes.objects.filter(
                user_id=request.user.id, video_id=video_id).delete()
            current_dislikes_count -= 1
        else:
            dislikes_obj = dislikes(
                user_id=request.user,
                video_id=video_info.objects.get(id=video_id),
            )
            dislikes_obj.save()
            if likes.objects.filter(user_id=request.user.id, video_id=video_id).exists():
                likes.objects.filter(user_id=request.user.id,
                                     video_id=video_id).delete()
                current_likes_count -= 1
            current_dislikes_count += 1
        data = {
            "likes_count": int(current_likes_count),
            "dislikes_count": int(current_dislikes_count),
        }
        return JsonResponse(data)


def main_comment(request):
    if request.method == "GET":
        video_id = int(request.GET['video_id'])
        comment_text = request.GET['comment_text']
        comments_obj = comments(
            user_id = request.user,
            video_id=video_info.objects.get(id=video_id),
            comment_text=comment_text,
            parent_comment_id = None,
        )
        comments_obj.save()
        print('comment saved')
        return HttpResponse('Comment Saved')


def test(request):
    form = video_creation_form()
    if request.method == 'POST':
        form = video_creation_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    context = {'form': form}
    return render(request, 'channel/index.html', context)
