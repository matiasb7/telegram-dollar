import requests
from telegram import Bot
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
COINS_API = 'https://api.bluelytics.com.ar/v2/latest'
TELEGRAM_API_TOKEN = os.environ.get('TELEGRAM_API_TOKEN')
BOT_USERNAME = '@dolar_daily_bot'
CHAT_ID = os.environ.get('CHAT_ID')


def get_coins():
    response = requests.get(COINS_API)
    dollar_blue = ''
    euro_blue = ''
    if response.status_code == 200:
        info = response.json()
        dollar_blue = info['blue']['value_avg']
        euro_blue = info['blue_euro']['value_avg']

    return dollar_blue, euro_blue


async def send_message(api_token, chat_id, message):
    bot = Bot(token=api_token)
    await bot.send_message(chat_id=chat_id, text=message)


dollar, euro = get_coins()
message = f"Dollar: {dollar}, Euro: {euro}"
asyncio.run(send_message(TELEGRAM_API_TOKEN, CHAT_ID, message))
