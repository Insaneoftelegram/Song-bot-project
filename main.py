import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from youtube_dl import YoutubeDL

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger(__name__)

# Define the start command handler
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I am a song download bot. Just send me the name of the song you want to download.")

# Define the message handler
def message_handler(update, context):
    song_name = update.message.text
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{song_name}", download=False)
        url = info['entries'][0]['formats'][0]['url']
        context.bot.send_audio(chat_id=update.effective_chat.id, audio=url)

# Define the main function
def main():
    # Create the updater and pass in your bot token
    updater = Updater(token=os.environ.get('5021398357:AAE62C4x-jptJ3S2gLpuHvrXru6xM5yIAa'), use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add the start command handler
    dispatcher.add_handler(CommandHandler("start", start))

    # Add the message handler
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
