import os
from dotenv import load_dotenv
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import messages
import data

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')


async def get_events(day=0):
    events = await data.get_data(day)
    message = ''
    if len(events) == 0:
        message = 'На сегодня нет спортивных событий'
    else:
        message = ' '.join(events)
    return message


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=messages.START)


async def today(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = await get_events(0)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)


async def tomorrow(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = await get_events(1)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)


async def after_tomorrow(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = await get_events(2)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)


if __name__ == '__main__':
    application = ApplicationBuilder().token(API_TOKEN).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    today_handler = CommandHandler('today', today)
    application.add_handler(today_handler)

    tomorrow_handler = CommandHandler('tomorrow', tomorrow)
    application.add_handler(tomorrow_handler)

    tomorrow_handler = CommandHandler('after_tomorrow', after_tomorrow)
    application.add_handler(tomorrow_handler)

    application.run_polling()
