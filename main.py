import logging
import os

from aiogram.dispatcher import Dispatcher, filters
from aiogram.utils.executor import start_webhook
from aiogram import Bot, types

from core.buttons import start_buttons, GET_CONTACT
from nova_bot.settings import dotenv_path, load_dotenv

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

TOKEN = os.environ.get('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')

# webhook settings
# WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_HOST = f' http://127.0.0.1'
WEBHOOK_PATH = f'/webhook/{TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)


async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dispatcher):
    await bot.delete_webhook()


@dp.message_handler(state='*', commands=['start'])
async def send_welcome(msg: types.Message) -> None:
    await msg.answer(
        f'Привет, {msg.from_user.first_name}, а дай номер',
        reply_markup=start_buttons,
    )


@dp.message_handler(filters.Text(equals=GET_CONTACT), state='*')
async def send_contact_info(msg: types.Message) -> None:
    await msg.answer('Спасибо, что поделился номером ✨ Все прошло успешно!')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )