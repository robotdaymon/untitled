from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    return render(request, 'base.html')


def common_table(request):
    return HttpResponse('<h1>Finally!</h1><h1>Finally!</h1><h1>Finally!</h1><h1>Finally!</h1>')


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('index/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html' , {'form': form})

