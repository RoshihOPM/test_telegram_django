import logging
from users.models import UserProfileModel
from polls.models import PollModel
from telegrambot.services.handlers.base_handler import BaseHandler

logger = logging.getLogger('telegrambot')


class PollAnswerHandler(BaseHandler):
    def handle(self, poll_answer):
        chat_id = poll_answer["user"]["id"]
        poll_id = poll_answer["poll_id"]
        option_ids = poll_answer["option_ids"]

        try:
            user = UserProfileModel.objects.get(telegram_chat_id=chat_id)
            poll = PollModel.objects.get(telegram_poll_id=poll_id)

            poll.user_options = option_ids
            poll.save()

            user.completed_polls += 1
            user.save()

            logger.info(f"Ответ от chat_id={chat_id} сохранён для опроса {poll_id}")

        except UserProfileModel.DoesNotExist:
            logger.warning(f"Пользователь с chat_id={chat_id} не найден")

        except PollModel.DoesNotExist:
            logger.warning(f"Опрос с telegram_poll_id={poll_id} не найден")

        except Exception as e:
            logger.exception(f"Ошибка в PollAnswerHandler: {e}")
