from pyrogram import Client, filters


API_ID = ""
API_HASH = ""
BOT_TOKEN = ""


INSANE = Client(
    name="insane test bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


@INSANE.on_message(filters.command("start")
async def start_cmd(Client, message):
    await message.reply_text("Hello......!!!")
 



print("Bot started ")
INSANE.run()

