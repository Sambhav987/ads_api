from django.contrib import admin
from django.urls import path, include
from fb import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='home'),
    # path('login/', views.index, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('campaigns/', views.campaigns, name='campaigns'),
    path('about/', views.about, name='about'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('oauth/', include('social_django.urls', namespace="social")),
]