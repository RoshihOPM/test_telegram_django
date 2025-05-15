from users.models import UserProfileModel


class UserService:
    @staticmethod
    def get_or_create_user(chat_id: int):
        return UserProfileModel.objects.get_or_create(telegram_chat_id=chat_id)

    @staticmethod
    def get_user(chat_id: int) -> UserProfileModel:
        return UserProfileModel.objects.get(telegram_chat_id=chat_id)

    @staticmethod
    def increment_completed_polls(user: UserProfileModel):
        user.completed_polls += 1
        user.save()
