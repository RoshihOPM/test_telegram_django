import logging
from users.models import UserProfileModel
from polls.models import PollModel
from telegrambot.services.handlers.base_handler import BaseHandler

logger = logging.getLogger('telegrambot')


class PollHandler(BaseHandler):
    def __init__(self, telegram_api):
        self.telegram_api = telegram_api

    def handle(self, chat_id):
        try:
            user = UserProfileModel.objects.get(telegram_chat_id=chat_id)
            poll = PollModel.objects.order_by("-created_at").first()

            if poll:
                response = self.telegram_api.send_poll(
                    chat_id,
                    poll.question,
                    poll.options
                    )

                poll_id = response.json().get("result", {}).get("poll", {}).get("id")

                if poll_id:
                    poll.telegram_poll_id = poll_id
                    poll.user_profile = user
                    poll.save()
                    logger.info(f"Опрос отправлен пользователю {chat_id} с poll_id={poll_id}")
                else:
                    logger.warning("Не удалось получить telegram_poll_id из ответа Telegram")
            else:
                logger.info(f"Нет доступных опросов для chat_id={chat_id}")
        except Exception as e:
            logger.exception(f"Ошибка в PollHandler: {e}")
