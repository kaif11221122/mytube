from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def homepage(request):
    if request.user.is_authenticated:
        return render(request, 'homepage/loggedin.html')
    else:
        return render(request, 'homepage/non_loggedin.html')
