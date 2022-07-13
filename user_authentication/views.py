from crypt import methods
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

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
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return render(request, 'homepage/index.html')
        else:
            return HttpResponse('wrong')
    else:
        form = AuthenticationForm()
    return render(request, 'user_authentication/login.html', {'form': form})
