import json
import logging
from django.http import JsonResponse
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

@csrf_exempt
def telegram_webhook(request):
    if request.method != "POST":
        logger.warning("Invalid method (not POST)")
        return JsonResponse({"error": "Invalid method"}, status=405)

    try:
        data = json.loads(request.body)
        logger.debug(f"Получен update: {data}")

    except Exception as e:
        logger.error(f"Ошибка парсинга JSON: {e}")
        return JsonResponse({"error": "Invalid JSON"}, status=400)

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

    return JsonResponse({"ok": True})
