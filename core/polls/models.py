from django.db import models
from users.models import UserProfileModel


# Create your models here.
class PollModel(models.Model):
    user_profile = models.ForeignKey(
        UserProfileModel,
        on_delete=models.CASCADE,
        related_name='user_polls',
        db_index=True
    )

    telegram_poll_id = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        db_index=True
    )
    
    question = models.TextField()
    options = models.JSONField(default=list, null=True, blank=True)
    user_options = models.JSONField(default=list, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Poll {self.telegram_poll_id}'
