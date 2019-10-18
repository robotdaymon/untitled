from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView
from django_tables2 import SingleTableView, LazyPaginator
from .models import Parceline, Person
from .tables import ParceTable, PersonTable


class ParcelineListView(ListView):
    model = Parceline
    table_class = ParceTable
    template_name = 'parcelines.html'
    paginator_class = LazyPaginator

def index(request):
    return render(request, 'index.html')


def common_table(request):
    return HttpResponse('<h1>Finally!</h1><h1>Finally!</h1><h1>Finally!</h1><h1>Finally!</h1>')


class PersonListView(SingleTableView):
    model = Person
    table_class = PersonTable
    template_name = 'people.html'