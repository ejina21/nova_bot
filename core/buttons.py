from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

GET_CONTACT = 'Поделиться номером 📞'


button_get_contact = KeyboardButton(GET_CONTACT, request_contact=True)

start_buttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)
start_buttons.add(button_get_contact)