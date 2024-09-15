import requests
from pyrogram import Client, filters
from pyrogram.types import Message,InlineKeyboardButton,InlineKeyboardMarkup
from pyrogram.enums import ChatAction
from info import BOT_USERNAME

DONATE_ARMY = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/DONATE_ARMY_ULTIMATE_FILTER_BOT?startgroup=true"),
    ],
]

@Client.on_message(filters.command("cosplay"))
async def cosplay(_,msg):
    img = requests.get("https://waifu-api.vercel.app").json()
    await msg.reply_photo(img, caption=f"ᴄᴏsᴘʟᴀʏ ʙʏ ᴅᴏɴᴀᴛᴇ_ᴀʀᴍʏ™", reply_markup=InlineKeyboardMarkup(DONATE_ARMY),)



@Client.on_message(filters.command("ncosplay"))
async def ncosplay(_,msg):
    if msg.chat.type != ChatType.PRIVATE:
      await msg.reply_text("❍ sᴏʀʀʏ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ɪɴ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ ᴡɪᴛʜ ʙᴏᴛ",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("ɢᴏ ᴘᴍ",url=f"https://t.me/{Client.me.username}?start=True")]
            ]
        ))
    else:
       ncosplay = requests.get("https://waifu-api.vercel.app/items/1").json()

       await msg.reply_photo(ncosplay, caption=f"ᴄᴏsᴘʟᴀʏ ʙʏ ᴅᴏɴᴀᴛᴇ_ᴀʀᴍʏ™", reply_markup=InlineKeyboardMarkup(DONATE_ARMY),)
