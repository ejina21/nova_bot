import json

from django.views import View
from main import bot, types
from django.http import JsonResponse

from nova_bot.settings import DEBUG


class UpdateBot(View):
    def post(self, request, *args, **kwargs):
        if DEBUG:
            bot.process_telegram_event(json.loads(request.body))
        else:
            bot.process_telegram_event.delay(json.loads(request.body))

        return JsonResponse({"ok": "POST request processed"})

    def get(self, request, *args, **kwargs):  # for debug
        return JsonResponse({"ok": "Get request received! But nothing done"})