from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('index/', index),
    path('common_table/', common_table),
    path('login/', login)
]
