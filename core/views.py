import json

from django.views import View
from main import bot, dp, types
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from nova_bot.settings import DEBUG


class UpdateBot(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(UpdateBot, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(json.loads(request.body))
        responce = json.loads(request.body)
        username = responce['chat']['username']
        print(username)
        dp.process_update(types.Update(**responce))
        # if DEBUG:
        #     bot.process_telegram_event(json.loads(request.body))
        # else:
        #     bot.process_telegram_event.delay(json.loads(request.body))

        return JsonResponse({"ok": "POST request processed"})

    def get(self, request, *args, **kwargs):  # for debug
        return JsonResponse({"ok": "Get request received! But nothing done"})