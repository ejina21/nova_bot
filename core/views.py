import json

from django.views import View

from core.buttons import start_buttons
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import requests

from core.static_texts import welcome, success
from nova_bot.settings import TOKEN


class UpdateBot(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(UpdateBot, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        responce = json.loads(request.body)
        message = responce['message']
        chat_id = message['chat']['id']
        if 'text' in message and message['text'] == '/start':
            name = message['chat']['first_name']
            self.send_message(chat_id, welcome.format(name))
        elif 'contact' in message:
            username = message['chat']['username']
            phone = message['contact']['phone_number']
            headers = {'Content-Type': 'application/json'}
            data = {'phone': phone,'login': username}
            requests.post('https://s1-nova.ru/app/private_test_python/', headers=headers, json=data)
            self.send_message(chat_id, success)
        return JsonResponse({"ok": "POST request processed"})

    def get(self, request, *args, **kwargs):  # for debug
        return JsonResponse({"ok": "Get request received! But nothing done"})

    @staticmethod
    def send_message(chat_id, text):
        method = "sendMessage"
        token = TOKEN
        url = f"https://api.telegram.org/bot{token}/{method}"
        data = {"chat_id": chat_id, "text": text, 'reply_markup': start_buttons}
        requests.post(url, data=data)