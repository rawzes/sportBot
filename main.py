import os
from dotenv import load_dotenv
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import messages


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=messages.START)


if __name__ == '__main__':
    application = ApplicationBuilder().token(API_TOKEN).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()
