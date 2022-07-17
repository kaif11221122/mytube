from unicodedata import name
from django.urls import path
from . import views
app_name = 'watch'
urlpatterns = [
    path('watch/<int:id>/', views.watch, name='watch'),
]
