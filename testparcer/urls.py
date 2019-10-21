from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('index/', index, name='index'),
    path('common_table/', common_table, name='common_table'),
    path('common_table_p/<int:page>', common_table_p, name='common_table_p'),
    path('top10/', top10, name='top10'),
    path('xlssave/', xlssave),
    path('aggregated/', aggregated, name='aggregated'),
    path('ip/<str:ip>', stats, name='stats'),
    path('get_data_by_year/<str:ip>', get_data_by_year, name='gdbi'),
    path(r'^(?P<task_id>[\w-]+)/$', get_progress, name='task_status'),
]
