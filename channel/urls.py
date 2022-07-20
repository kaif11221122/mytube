from django.urls import path
from . import views

urlpatterns = [
    path('channel/', views.test, name="channel"),
    path('like/', views.like, name='like'),
    path('dislike/', views.dislike, name='dislike'),
    path('main_comment/',views.main_comment, name='main_comment'),
]
