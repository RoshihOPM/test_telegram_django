from django.urls import path
from telegrambot.views import telegram_webhook


urlpatterns = [
    path('webhook', telegram_webhook, name='telegram_webhook')
]
