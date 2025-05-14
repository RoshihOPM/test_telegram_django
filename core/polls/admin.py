from django.contrib import admin
from .models import PollModel


# Register your models here.
@admin.register(PollModel)
class PollModelAdmin(admin.ModelAdmin):
    list_display = ['question', 'telegram_poll_id', 'user_profile', 'created_at']
    search_fields = ['question', 'telegram_poll_id']
    list_filter = ['created_at']
