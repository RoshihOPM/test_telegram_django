import json
import requests


class TelegramApi:
    def __init__(self, token):
        self.api_url = f"https://api.telegram.org/bot{token}/"

    def send_message(self, chat_id, text):
        return requests.post(
            f'{self.api_url}sendMessage',
            data={
                'chat_id': chat_id,
                'text': text
                }
            )

    def send_poll(self, chat_id, question, options):
        return requests.post(
            f'{self.api_url}sendPoll',
            data={
                'chat_id': chat_id,
                'question': question,
                'options': json.dumps(options),
                'is_anonymous': False
            }
        )
