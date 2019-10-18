from django.urls import path
from .views import PersonListView, ParcelineListView, index

urlpatterns = [
    path('', index),
    path('index/', index),
    path('common_table/', ParcelineListView.as_view()),
    # path("people/", PersonListView.as_view())
    path("people/", PersonListView.as_view())
]
