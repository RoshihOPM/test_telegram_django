import logging
from telegrambot.services.handlers.base_handler import BaseHandler
from telegrambot.services.user_service import UserService
from telegrambot.services.poll_service import PollService
from users.models import UserProfileModel
from polls.models import PollModel


logger = logging.getLogger("telegrambot")


class PollAnswerHandler(BaseHandler):
    def handle(self, poll_answer):
        chat_id = poll_answer["user"]["id"]
        poll_id = poll_answer["poll_id"]
        option_ids = poll_answer["option_ids"]

        try:
            user = UserService.get_user(chat_id)
            PollService.save_poll_answer(poll_id, user, option_ids)
            UserService.increment_completed_polls(user)

            logger.info(f"Ответ от chat_id={chat_id} сохранён для опроса {poll_id}")

        except UserProfileModel.DoesNotExist:
            logger.warning(f"Пользователь с chat_id={chat_id} не найден")

        except PollModel.DoesNotExist:
            logger.warning(f"Опрос с telegram_poll_id={poll_id} не найден")

        except Exception as e:
            logger.exception(f"Ошибка в PollAnswerHandler: {e}")
