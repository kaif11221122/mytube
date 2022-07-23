from django.shortcuts import redirect, render
from .forms import video_creation_form
from django.http import HttpResponse, JsonResponse
from watch.models import likes, dislikes, comments
from user_authentication.models import user_data
from .models import video_info
from django.core import serializers

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
        user_data_obj = user_data.objects.get(id=request.user.id)

        video_id = int(request.GET['video_id'])
        comment_text = request.GET['comment_text']
        comments_count = int(request.GET['comments_count'])
        comments_obj = comments(
            user_id=user_data_obj,
            video_id=video_info.objects.get(id=video_id),
            comment_text=comment_text,
            parent_comment_id=None,
        )
        comments_obj.save()
        queryset = comments.objects.filter(
            video_id=request.GET['video_id'], parent_comment_id=None).select_related('user_id')
        video_comments = serializers.serialize('json', queryset)
        data = {
            "video_comments": video_comments,
            "comments_count": comments_count+1,
        }
        return JsonResponse(data)


def replied_comment(request):

    if request.method == "GET":
        parent_comment_id = request.GET['parent_comment_id']
        parent_comment_obj = comments.objects.get(id=parent_comment_id)
        replied_comment_text = request.GET['replied_comment_text']
        video_id = int(request.GET['video_id'])

        user_data_obj = user_data.objects.get(id=request.user.id)
        comments_obj = comments(
            user_id=user_data_obj,
            video_id=video_info.objects.get(id=video_id),
            comment_text=replied_comment_text,
            parent_comment_id=parent_comment_obj,
        )
        comments_obj.save()
        queryset = comments.objects.filter(
            video_id=request.GET['video_id'], parent_comment_id=parent_comment_obj
        ).select_related('user_id')
        comment_replies = serializers.serialize('json', queryset)
        data = {"comment_replies": comment_replies}
        return JsonResponse(data)


def view_old_replies(request):
    if request.method == "GET":
        print('okkkkk')
        parent_comment_id = request.GET['parent_comment_id']
        parent_comment_obj = comments.objects.get(id=parent_comment_id)
        queryset = comments.objects.filter(
            parent_comment_id=parent_comment_obj).select_related('user_id')
        print(str(queryset.query))
        print('\n\n\nok')
        comments_replies_for_parent = []
        for obj in queryset:
            obj_dict = obj.__dict__
            obj_dict['username'] = str(obj.user_id.username)
            obj_dict['profile_image'] = obj.user_id.profile_image.url
            del obj_dict['_state']
            comments_replies_for_parent.append(obj_dict)
            print(obj_dict, '\n\n')
        data = {
            "comments_replies_for_parent": comments_replies_for_parent,
        }
        return JsonResponse(data)

# def subscribe_channel()


def test(request):
    form = video_creation_form()
    if request.method == 'POST':
        form = video_creation_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    context = {'form': form}
    return render(request, 'channel/index.html', context)
