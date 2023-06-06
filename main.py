from pyrogram import Client, filters


API_ID = "5642193"
API_HASH = "c28fc9ac88530587236175da89184d75"
BOT_TOKEN = "6297344590:AAFbBHK9PioaIS0sZnH0jR4a4Sp7859Rt_4"


INSANE = Client(
    name="insane test bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

 
print("Bot started ")
INSANE.run()

