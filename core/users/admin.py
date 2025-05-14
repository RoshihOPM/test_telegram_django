from django.contrib import admin
from .models import UserProfileModel


# Register your models here.
@admin.register(UserProfileModel)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['telegram_chat_id', 'completed_polls']
    search_fields = ['telegram_chat_id']
