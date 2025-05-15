from django.db import models


# Create your models here.
class UserProfileModel(models.Model):
    telegram_chat_id = models.BigIntegerField(unique=True, db_index=True)
    completed_polls = models.PositiveIntegerField(default=0)
    passed_polls = models.ManyToManyField(
        "polls.PollModel",
        related_name="users_passed",
        blank=True
        )

    def __str__(self):
        return f'User {self.telegram_chat_id}'
