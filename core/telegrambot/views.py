import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from telegrambot.services.telegram_api import TelegramApi
from telegrambot.services.handlers.start_handler import StartHandler
from telegrambot.services.handlers.poll_handler import PollHandler
from telegrambot.services.handlers.poll_answer_handler import PollAnswerHandler
from telegrambot.config import BOT_TOKEN


logger = logging.getLogger('telegrambot')
telegram_api = TelegramApi(BOT_TOKEN)

COMMAND_HANDLERS = {
    "/start": StartHandler(telegram_api),
    "/poll": PollHandler(telegram_api),
}

@method_decorator(csrf_exempt, name='dispatch')
class TelegramWebhookView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            logger.debug(f"Получен update: {data}")
        except Exception as e:
            logger.error(f"Ошибка парсинга JSON: {e}")
            return Response({"error": "Invalid JSON"}, status=status.HTTP_400_BAD_REQUEST)

        if "message" in data:
            chat_id = data["message"]["chat"]["id"]
            text = data["message"].get("text", "")

            handler = COMMAND_HANDLERS.get(text)
            if handler:
                handler.handle(chat_id)
            else:
                logger.info(f"Неизвестная команда от chat_id={chat_id}: {text}")

        elif "poll_answer" in data:
            PollAnswerHandler().handle(data["poll_answer"])

        return Response({"ok": True}, status=status.HTTP_200_OK)
