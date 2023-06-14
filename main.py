from pyrogram import Client, filters

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from logger import Logger
import os
import youtube_dl
from googleapiclient.discovery import build

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
VIDEO = 'youtube#video'
YOUTUBE_VIDEO_URL = 'https://www.youtube.com/watch?v='
VERSION = '3.0.1'
YOUTUBE_API_SECRET = os.environ.get('YOUTUBE_DEV_KEY')

logger = Logger('youtube')

class YdlLogger(object):
    def info(self, msg):
        pass

    def debug(self, msg):
        pass

    def warning(self, msg):
        logger.warning(msg)

    def error(self, msg):
        logger.error(msg)
        
def get_youtube_url(query):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=YOUTUBE_API_SECRET)
    search_response = youtube.search().list(q=query, part='id, snippet').execute()
    for item in search_response['items']:
        if item['id']['kind'] == 'youtube#video':
            return YOUTUBE_VIDEO_URL + item['id']['videoId']
        
def progreess_hook(d):
    if d['status'] == 'finished':
        logger.info(f'Done downloading: {d} now Converting...')
        print('--->\t[Done]')

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': YdlLogger(),
    'progress_hooks': [progreess_hook],
}
        
def download_mp3(search_term, title, album):
    ydl_opts_ext = ydl_opts
    ydl_opts_ext['outtmpl'] = f"Downloads/{title} - {album}.%(ext)s"
    print(f"Trying to Download '{title}' from '{album}' album...", end='\t')
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([get_youtube_url(search_term)])
    except:
        print(f"failed to download {title}...")
        logger.error(f"failed to download {title}...")

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
    InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/INSANEX3_SUPPORT")
    ]]

@INSANE.on_message(filters.command("start"))
async def start_cmd(Client, message):
    await message.reply_photo(
        photo="https://telegra.ph/file/da545a93169c6e91d4c98.jpg",
        caption="ʜᴇʏ, \n Bot under maintenance....!! \n \n ɪ'ᴍ ᴀ ᴛᴇʟᴇɢʀᴀᴍ sᴛʀᴇᴀᴍɪɴɢ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇ. sᴜᴘᴘᴏʀᴛɪɴɢ ᴘʟᴀᴛғᴏʀᴍs ʟɪᴋᴇ ʏᴏᴜᴛᴜʙᴇ,ʀᴇssᴏ....ᴇᴛᴄ \n \n A ᴘᴏᴡᴇғᴜʟ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ᴀɴᴅ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs.",
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


                              
                              
                            
 
print("INSANE Bot started ")
INSANE.run()

