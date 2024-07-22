from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', signup, name= "signup"),
    path('login/', login, name='login'),
    path('logout/', custom_logout_view, name='logout'),
    path('home/', home, name= "home"),
]