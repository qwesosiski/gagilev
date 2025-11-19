from django.shortcuts import render, HttpResponse
from .models import *

def main(request):
    return render(request, 'main.html')

def all(request):
    return render(request, 'all.html')

def premium(request):
    return render(request, 'premium.html')