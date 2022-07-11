import json

from core.buttons import start_buttons
from core.models import UserProfile
from core.static_texts import welcome, success, error, already_exist, exist_not_contact
from nova_bot.settings import TOKEN
import requests


def send_message(chat_id: int, text: str, is_button=False) -> None:
    method = "sendMessage"
    token = TOKEN
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = {"chat_id": chat_id, "text": text}
    if is_button:
        data['reply_markup'] = start_buttons
    requests.post(url, data=data)


def send_welcome(message: json) -> None:
    name = message['chat']['first_name']
    username = message['chat']['username']
    chat_id = message['chat']['id']
    user, created = UserProfile.objects.get_or_create(
        tg_id=chat_id,
        username=username,
    )
    if created:
        send_message(chat_id, welcome.format(name), is_button=True)
    elif user.is_get_contact:
        send_message(chat_id, already_exist)
    else:
        send_message(chat_id, exist_not_contact, is_button=True)


def send_contact_to_api(message: json) -> None:
    username = message['chat']['username']
    chat_id = message['chat']['id']
    phone = message['contact']['phone_number']
    headers = {'Content-Type': 'application/json'}
    data = {'phone': phone, 'login': username}
    user = UserProfile.objects.get(tg_id=chat_id)
    responce = requests.post('https://s1-nova.ru/app/private_test_python/', headers=headers, json=data)
    if responce.status_code == 200:
        send_message(chat_id, success)
        user.is_get_contact = True
        user.save()
    else:
        send_message(chat_id, error, is_button=True)
