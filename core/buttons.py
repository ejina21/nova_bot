import json

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

GET_CONTACT = 'Поделиться номером 📞'


button_get_contact = KeyboardButton(GET_CONTACT, request_contact=True)
reply_markup = {
    'keyboard': [[{
        'text': GET_CONTACT,
        'request_contact': True
    }]],
    'resize_keyboard': True,
    'one_time_keyboard': True
}
start_buttons = json.dumps(reply_markup)
