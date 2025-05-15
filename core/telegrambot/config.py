import os
from dotenv import load_dotenv

load_dotenv(override=True)

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not BOT_TOKEN:
    raise EnvironmentError("TELEGRAM_BOT_TOKEN not found")
