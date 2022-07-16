from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout
from .models import user_data
from .forms import RegisterUserForm
from django.contrib.auth.models import User
# Create your views here.


def register(request):
    if request.user.id is None:
        if request.method == "POST":
            form = RegisterUserForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                instance_user_data = user_data(
                    username=User.objects.get(
                        username=request.POST["username"]),
                    profile_image=request.FILES['profile_image'],
                )
                instance_user_data.save()
                return redirect('login')
        else:
            form = RegisterUserForm()
        return render(request, 'user_authentication/registeration.html', {'form': form})
    else:
        return redirect('homepage')


def login(request):
    if request.user.id is None:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']
                user_password = form.cleaned_data['password']
                user = authenticate(username=user_name, password=user_password)
                if user is not None:
                    auth_login(request, user)
                    return redirect('homepage')
                else:
                    return HttpResponse('unable to authenticate !!!!!')
            else:
                return HttpResponse('wrong')
        else:
            form = AuthenticationForm()
        return render(request, 'user_authentication/login.html', {'form': form})
    else:
        return redirect('homepage')


def logout_user(request):
    if request.user.id is not None:
        logout(request)
        return redirect('homepage')
    return redirect('homepage')
