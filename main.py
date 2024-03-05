from dotenv import load_dotenv
from telegram.ext import Updater, MessageHandler, Filters
from telegram import InputFile
import download_from_youtube
import os

load_dotenv()
token = os.getenv("Token")

def get_url(update, context):
    url = update.message.text
    try:
        val = download_from_youtube.download_audio(url)
        with open(val, 'rb') as audio_file:
            context.bot.send_audio(
                chat_id=update.effective_chat.id,
                audio=InputFile(audio_file)
            )
        os.remove(val)
        print("Audio send succesfully")
    except Exception as e:
        print("Error:", str(e))

updater = Updater(token, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(Filters.text, get_url))

updater.start_polling()
updater.idle()

