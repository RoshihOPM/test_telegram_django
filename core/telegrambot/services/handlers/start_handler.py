import logging
from telegrambot.services.handlers.base_handler import BaseHandler
from telegrambot.services.user_service import UserService


logger = logging.getLogger("telegrambot")


class StartHandler(BaseHandler):
    def __init__(self, telegram_api):
        self.telegram_api = telegram_api

    def handle(self, chat_id):
        user, created = UserService.get_or_create_user(chat_id)
        logger.info(f"{'Создан' if created else 'Найден'} пользователь chat_id={chat_id}")
        self.telegram_api.send_message(chat_id, "Добро пожаловать!")
