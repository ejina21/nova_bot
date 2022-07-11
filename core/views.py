import json

from django.views import View

from core.buttons import start_buttons
from main import bot, dp, types
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import requests
from django.http import HttpResponse
from aiogram.dispatcher.webhook import SendMessage

from nova_bot.settings import TOKEN


async def index(request):
    responce = json.loads(request.body)
    username = responce['message']['chat']['username']
    name = responce['message']['chat']['first_name']
    chat_id = responce['message']['chat']['id']
    print(responce)
    print(username)
    await bot.send_message(
        chat_id=chat_id,
        text=f'Привет, {name}, а дай номер',
        reply_markup=start_buttons,
    )
    return HttpResponse("POST request processed")


class UpdateBot(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(UpdateBot, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(json.loads(request.body))
        responce = json.loads(request.body)
        username = responce['message']['chat']['username']
        name = responce['message']['chat']['first_name']
        chat_id = responce['message']['chat']['id']
        print(responce)
        return SendMessage(
            chat_id=chat_id,
            text=f'Привет, {name}, а дай номер',
            reply_markup=start_buttons,
        )
        # return JsonResponse({"ok": "POST request processed"})

    def get(self, request, *args, **kwargs):  # for debug
        return JsonResponse({"ok": "Get request received! But nothing done"})

    @staticmethod
    def send_message(chat_id, text):
        method = "sendMessage"
        token = TOKEN
        url = f"https://api.telegram.org/bot{token}/{method}"
        data = {"chat_id": chat_id, "text": text}
        requests.post(url, data=data)