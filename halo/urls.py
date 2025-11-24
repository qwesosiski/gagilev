from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .views import main, all, premium, settings

urlpatterns = [
    path('', all, name= 'all'),
    path('premium', premium ,name = 'premium'),
    path('settings', settings ,name = 'settings')
]
