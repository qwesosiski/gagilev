from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .views import main, all

urlpatterns = [
    path('', all),
]
