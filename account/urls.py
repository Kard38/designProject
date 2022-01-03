from django.urls import path
from .views import login_view,userdetail_view, register_view, logout_view

app_name = 'account'
urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('userdetail/', userdetail_view, name='userdetail'),

]
