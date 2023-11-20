from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('log', views.log, name='log'),
    path('signup', views.signup, name='signup'),
    path('login', views.loginn, name='login'),

]
