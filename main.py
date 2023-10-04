from dotenv import load_dotenv
from telegram.ext import Application
import os
from bot.bot import Bot

if __name__ == '__main__':
    load_dotenv()
    TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
    app = Application.builder().token(TELEGRAM_API_TOKEN).build()
    controller = Bot(app)
    app.run_polling(poll_interval=3)
