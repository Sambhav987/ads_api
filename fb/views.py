import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import User

from . import fbads

user_data = None

# Create your views here.
def index(request):
    # if request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse("dashboard"))
    if request.method == "POST":
        pass
    
    if user_data is None:
        return render(request, 'fb/index.html')
    else:
        return redirect('dashboard/')

# def login(request):
#     return render(request, 'fb/index.html')

def about(request):
    return render(request, 'fb/about.html')


def dashboard(request):
    return render(request, "fb/dashboard.html")


def campaigns(request):
    context = fbads.getCampaigns(request, User)
    if context is not None:
        return render(request, "fb/campaigns.html", context)
    
    else:
        return HttpResponseRedirect('/fb/', {"message_type" : "danger", "message" : "Error in retrieving campaigns!"})