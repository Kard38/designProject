from django.urls import path
from .views import *

app_name = 'game'
urlpatterns = [
    path('', game_index, name='index'),
    path('<int:id>/detail', game_detail, name='detail'),
    path('category/', game_cat, name='category'),
    path('userfavorite/', user_favorite, name='userfavorite'),

]
