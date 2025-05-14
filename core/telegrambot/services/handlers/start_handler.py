import logging
from users.models import UserProfileModel
from telegrambot.services.handlers.base_handler import BaseHandler

logger = logging.getLogger('telegrambot')


class StartHandler(BaseHandler):
    def __init__(self, telegram_api):
        self.telegram_api = telegram_api

    def handle(self, chat_id):
        user, created = UserProfileModel.objects.get_or_create(
            telegram_chat_id=chat_id
            )
        logger.info(f"{'Создан' if created else 'Найден'} пользователь chat_id={chat_id}")
        self.telegram_api.send_message(chat_id, "Добро пожаловать!")
