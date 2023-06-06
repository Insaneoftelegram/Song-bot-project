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
    InlineKeyboardButton("ADD ME YOUR GROUP", url="t.me/insanex3"),
    InlineKeyboardButton("Owner", url="t.me/insane_of_telegram"),
    InlineKeyboardButton("Source", url="t.me/insanex3")
    ]]

@INSANE.on_message(filters.command("start"))
async def start_cmd(Client, message):
    await message.reply_text(
        text="hello",
        reply_markup =InlineKeyboardMarkup (START_BUTTONS)
    )
                              
                              
                            
 
print("INSANE Bot started ")
INSANE.run()

