import os
import requests
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

if not BOT_TOKEN or not WEBHOOK_URL:
    raise Exception("BOT_TOKEN или WEBHOOK_URL не указаны в .env")

url = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook"
response = requests.get(url, params={"url": WEBHOOK_URL})

print(response.status_code)
print(response.json())
