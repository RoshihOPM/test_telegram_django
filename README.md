# 🤖 Telegram-бот для опросов (Django + Telegram Bot API)

## 📌 Описание

Проект реализует Telegram-бота на Django, который позволяет:

- Регистрировать пользователей при команде `/start`
- Отправлять им последний созданный опрос при `/poll`
- Принимать и сохранять их ответы через Telegram Webhook

> Используется только `requests` — без сторонних Telegram-библиотек.

---

## 🧱 Стек технологий

- Django 4+
- Python 3.10+
- requests
- Telegram Bot API (нативный)
- Webhook
- dotenv
- (по желанию) ngrok для локального теста

---

## ⚙️ Установка

### 1. Клонируй репозиторий

```bash
git clone https://github.com/RoshihOPM/test_telegram_django.git
cd core
```

### 2. Установи зависимости

pip install -r requirements.txt

### 3. Настрой .env
Создай файл .env в корне проекта

TELEGRAM_BOT_TOKEN=your_bot_token

### 4. Сделай миграции и создай суперпользователя

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
