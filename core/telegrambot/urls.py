from django.urls import path
from telegrambot.views import TelegramWebhookView


urlpatterns = [
    path('webhook', TelegramWebhookView.as_view(), name='telegram_webhook')
]
