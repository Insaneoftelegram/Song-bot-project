from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
import telebot
from telebot import types
import requests

API_ID = "5642193"
API_HASH = "c28fc9ac88530587236175da89184d75"
BOT_TOKEN = "6088570842:AAEP-Stzkhzj53aijcDOeDbhs-hZo9qjeLU"


INSANE = Client(
    name="insane test bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

START_BUTTONS =[[
    InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url="https://t.me/Resso_offical_bot?startgroup=true")
    ],[
    InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="t.me/INSANEX3"),
    InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/RESSO_SUPPORT")
    ]]

@INSANE.on_message(filters.command("start"))
async def start_cmd(Client, message):
    await message.reply_photo(
        photo="https://telegra.ph/file/da545a93169c6e91d4c98.jpg",
        caption="ʜᴇʏ, \n \n \n ɪ'ᴍ ᴀ ᴛᴇʟᴇɢʀᴀᴍ sᴛʀᴇᴀᴍɪɴɢ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇ. sᴜᴘᴘᴏʀᴛɪɴɢ ᴘʟᴀᴛғᴏʀᴍs ʟɪᴋᴇ ʏᴏᴜᴛᴜʙᴇ,ʀᴇssᴏ....ᴇᴛᴄ \n \n A ᴘᴏᴡᴇғᴜʟ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ᴀɴᴅ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs.\n maintenance work loading..........",
        reply_markup =InlineKeyboardMarkup (START_BUTTONS)
  
    )
    
INSANE_BUTTONS =[[
    InlineKeyboardButton("Owner", url="https://t.me/insanex3")
    ]]
    
@INSANE.on_message(filters.command("owner"))
async def owner_cmd(client, message):
    await message.reply_photo(
        photo="https://telegra.ph/file/a42e0a1e09e4ca442fe3b.jpg",
        reply_markup =InlineKeyboardMarkup (INSANE_BUTTONS)
    )


# Handle the /help command
@INSANE.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "To download a song, simply type the name of the song.")

# Handle text messages
@INSANE.message_handler(func=lambda message: True)
def handle_message(message):
    song_name = message.text
    download_song(song_name, message.chat.id)

# Download the song
def download_song(song_name, chat_id):
    # Search for the song using an API or web scraping
    # Replace the following line with your own code to search for the song
    search_results = search_song(song_name)

    # Get the download link for the first search result
    download_link = search_results[0]['download_link']

    # Download the song
    response = requests.get(download_link)
    file_name = song_name + '.mp3'

    # Save the song to a file
    with open(file_name, 'wb') as f:
        f.write(response.content)

    # Send the song file to the chat group
    with open(file_name, 'rb') as f:
        bot.send_audio(chat_id, f)

    # Delete the song file
    os.remove(file_name)

# Search for the song using an API or web scraping
def search_song(song_name):
    # Replace the following line with your own code to search for the song
    # You can use APIs like Spotify, SoundCloud, or web scraping techniques
    search_results = [
        {
            'title': 'Song Title',
            'artist': 'Artist Name',
            'download_link': 'https://example.com/song.mp3'
        }
    ]

    return search_results
    
 
print("INSANE Bot started ")
INSANE.run()
