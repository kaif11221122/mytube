from django.urls import path
from . import views

urlpatterns = [
    path('channel/', views.test, name="channel"),
    path('like/', views.like, name='like'),
    path('dislike/', views.dislike, name='dislike'),
    path('main_comment/', views.main_comment, name='main_comment'),
    path('replied_comment/', views.replied_comment, name='replied_comment'),
    path('view_old_replies/', views.view_old_replies, name='view_old_replies'),
]
