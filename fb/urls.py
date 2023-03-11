from django.contrib import admin
from django.urls import path
from fb import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('login/', views.index, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('campaigns/', views.campaigns, name='campaigns'),
    path('about/', views.about, name='about'),
]