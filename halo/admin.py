from django.contrib import admin
from .models import Subscription, User, Message, Chat, Channel

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'validity_period']
    list_filter = ['title']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone_number', 'subscription']
    list_filter = ['subscription']
    search_fields = ['username', 'email']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'text', 'sending_time']
    list_filter = ['sending_time']
    search_fields = ['text']

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    filter_horizontal = ['users', 'messages']

@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'description']
    filter_horizontal = ['messages']