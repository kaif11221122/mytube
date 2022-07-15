from crypt import methods
from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout
# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'user_authentication/registeration.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_password = form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Logged in success !!!')
                return redirect('homepage')
            else:
                return HttpResponse('unable to authenticate !!!!!')
        else:
            return HttpResponse('wrong')
    else:
        form = AuthenticationForm()
    return render(request, 'user_authentication/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('homepage')
