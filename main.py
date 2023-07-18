from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = "5642193"
API_HASH = "c28fc9ac88530587236175da89184d75"
BOT_TOKEN = "5208962076:AAFRivp9NqIABXvc0m8FI7PFxtaViYQeyeM"


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
        caption="ʜᴇʏ, \n \n \n ɪ'ᴍ ᴀ ᴛᴇʟᴇɢʀᴀᴍ sᴛʀᴇᴀᴍɪɴɢ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇ. sᴜᴘᴘᴏʀᴛɪɴɢ ᴘʟᴀᴛғᴏʀᴍs ʟɪᴋᴇ ʏᴏᴜᴛᴜʙᴇ,ʀᴇssᴏ....ᴇᴛᴄ \n \n A ᴘᴏᴡᴇғᴜʟ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ᴀɴᴅ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs.",
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

