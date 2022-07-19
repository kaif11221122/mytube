from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import video_creation_form

# Create your views here.


def test(request):
    form = video_creation_form()
    if request.method == 'POST':
        form = video_creation_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    context = {'form': form}
    return render(request, 'channel/index.html', context)
