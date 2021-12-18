from django.urls import path
from .views import *

app_name = 'game'
urlpatterns = [
    path('index', game_index, name='index'),
    path('<int:id>/detail', game_detail, name='detail')
]
