import json

from django.views import View

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from core.bot_services import send_welcome, send_contact_to_api


class UpdateBot(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(UpdateBot, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        responce = json.loads(request.body)
        message = responce['message']
        if 'text' in message and message['text'] == '/start':
            send_welcome(message)
        elif 'contact' in message:
            send_contact_to_api(message)
        return JsonResponse({"ok": "POST request processed"})
