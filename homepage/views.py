from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def homepage(request):
    if request.user.is_authenticated:
        print('Yesssssssssssssssssssss')
        print(f"Username --> {request.user.username}")
        return render(request, 'homepage/loggedin.html')
    else:
        print('Noooooooooooooooooooooo')
        return render(request, 'homepage/non_loggedin.html')
