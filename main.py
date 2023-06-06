from pyrogram import Client, filters

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



API_ID = "5642193"
API_HASH = "c28fc9ac88530587236175da89184d75"
BOT_TOKEN = "6297344590:AAFbBHK9PioaIS0sZnH0jR4a4Sp7859Rt_4"


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
    await message.reply_text(
        text="ʜᴇʏ,ᴍʏ ɴᴀᴍᴇ ɪs ʀᴇssᴏ ʙᴏᴛ. \n \n ɪ'ᴍ ᴀ ᴛᴇʟᴇɢʀᴀᴍ sᴛʀᴇᴀᴍɪɴɢ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇ. sᴜᴘᴘᴏʀᴛɪɴɢ ᴘʟᴀᴛғᴏʀᴍs ʟɪᴋᴇ ʏᴏᴜᴛᴜʙᴇ,ʀᴇssᴏ....ᴇᴛᴄ \n \n A ᴘᴏᴡᴇғᴜʟ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ᴀɴᴅ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs.",
        reply_markup =InlineKeyboardMarkup (START_BUTTONS)
    )
                              
                              
                            
 
print("INSANE Bot started ")
INSANE.run()

