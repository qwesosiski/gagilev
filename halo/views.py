from django.shortcuts import render, HttpResponse
from .models import *

def main(request):
    return render(request, 'main.html')

def all(request):
    users = User.objects.all().order_by('id')
    user = users.first() if users.exists() else None
    return render(request, 'all.html',{'User': user})

def premium(request):
    return render(request, 'premium.html')

def settings(request):
    return render(request, 'settings.html')