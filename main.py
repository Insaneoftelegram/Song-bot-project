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

@INSANE.on_message(filters.command("start"))
async def start_cmd(Client, message):
    await message.reply_text("ʜᴇʏ , 🖤

   ᴛʜɪs ɪs Resso 🥀

 ᴀ ᴩᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ᴩʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ᴀɴᴅ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs.

ᴀʟʟ ᴏғ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs ᴀʀᴇ ʟɪsᴛᴇᴅ ɪɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ.")
 
print("INSANE Bot started ")
INSANE.run()

