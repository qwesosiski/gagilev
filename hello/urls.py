from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .views import main

urlpatterns = [
    path('', main),
]
