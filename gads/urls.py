from django.contrib import admin
from django.urls import path
from gads import views

urlpatterns = [
    path('', views.index, name='Home'),
]