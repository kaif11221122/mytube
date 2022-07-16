from django.http import HttpResponse
from django.shortcuts import render
from user_authentication.models import user_data
# Create your views here.


def homepage(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        image = user_data.objects.filter(username_id=request.user.id)[0]
        return render(request, 'homepage/loggedin.html', {'image':image})
    else:
        return render(request, 'homepage/non_loggedin.html')
