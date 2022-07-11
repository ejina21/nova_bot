import json


GET_CONTACT = 'Поделиться номером 📞'


reply_markup = {
    'keyboard': [[{
        'text': GET_CONTACT,
        'request_contact': True
    }]],
    'resize_keyboard': True,
    'one_time_keyboard': True,
}
start_buttons = json.dumps(reply_markup)
