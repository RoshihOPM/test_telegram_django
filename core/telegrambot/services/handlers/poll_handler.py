import logging
from users.models import UserProfileModel
from telegrambot.services.handlers.base_handler import BaseHandler
from telegrambot.services.poll_service import PollService


logger = logging.getLogger('telegrambot')


class PollHandler(BaseHandler):
    def __init__(self, telegram_api):
        self.telegram_api = telegram_api

    def handle(self, chat_id):
        try:
            user = UserProfileModel.objects.get(telegram_chat_id=chat_id)
            poll = PollService.get_next_poll_for_user(user)

            if poll:
                response = self.telegram_api.send_poll(chat_id, poll.question, poll.options)
                poll_id = response.json().get("result", {}).get("poll", {}).get("id")

                if poll_id:
                    PollService.mark_poll_sent(poll, user, poll_id)
                    logger.info(f"Опрос отправлен пользователю {chat_id} с poll_id={poll_id}")
                else:
                    logger.warning("Не удалось получить telegram_poll_id из ответа Telegram")
            else:
                self.telegram_api.send_message(chat_id, "Вы прошли все доступные опросы 🎉")
                logger.info(f"Нет доступных опросов для chat_id={chat_id}")

        except UserProfileModel.DoesNotExist:
            logger.warning(f"Пользователь с chat_id={chat_id} не найден")
        except Exception as e:
            logger.exception(f"Ошибка в PollHandler: {e}")
