from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    return render(request, 'index.html')


def common_table(request):
    return HttpResponse('<h1>Finally!</h1><h1>Finally!</h1><h1>Finally!</h1><h1>Finally!</h1>')


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('index/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(request, username=username, password=password)
    # if user is not None:
    #     login(request, user)
    # else:
    #     return render(request, 'index.html')

