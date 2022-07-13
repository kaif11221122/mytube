from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def login(request):
    if request.method=='POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            return HttpResponse('correct')
        else:
            return HttpResponse('wrong')
    else:
        form = AuthenticationForm()
    return render(request, 'user_authentication/index.html', {'form':form})