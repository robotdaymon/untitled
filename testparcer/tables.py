import django_tables2 as tables
from .models import Parceline, Person

class ParceTable(tables.Table):
    class Meta:
        model = Parceline
        template_name = "django_tables2/bootstrap.html"
        fields = ("ipaddr","dtimefield",)

class PersonTable(tables.Table):
    class Meta:
        model = Person
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", )