from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_photo(
        chat_id=msg.chat.id,
        photo="https://files.catbox.moe/flwxix.jpg",
        caption=f"""✦ » ʜᴇʏ  {msg.from_user.mention}  ✤,
✦ » ɪ ᴀᴍ{me2},

✦ » 𝗞𝗦𝗗 𝗦𝗲𝗿𝘃𝗶𝗰𝗲 𝗦𝗲𝗹𝗹 𝗕𝗼𝘁.

✦ » Pʟᴇᴀsᴇ Cʜᴏᴏsᴇ Tʜᴇ Sᴇʀᴠɪᴄᴇs Aɴᴅ I Wɪʟʟ Gᴜɪᴅᴇ Yᴏᴜ ʜᴏᴡ ᴛᴏ Bᴜʏ A Sᴇʀᴠɪᴄᴇ ғʀᴏᴍ KSD Sᴇʀᴠɪᴄᴇ Sᴇʟʟ Bᴏᴛ.

✦ » ɪғ ʏᴏᴜ ɴᴇᴇᴅ ᴀɴʏ ʜᴇʟᴘ, ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ: [•⊹٭𝙺𝚂𝙳٭⊹•](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="▪ 𝗦𝗲𝗿𝘃𝗶𝗰𝗲'𝘀 ▪️", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("🔸 sᴜᴘᴘᴏʀᴛ🔸", url="https://t.me/TEAM_RIYA_SUPPORT"),
                    InlineKeyboardButton("▫️ ᴜᴘᴅᴀᴛᴇs▫️", url="https://t.me/KSD_BOT_NETWORK")
                ],
                [
                    InlineKeyboardButton("🔸 Aᴅᴅ Mᴇ Bᴀʙʏ 🔸", url="https://t.me/Olivia_xmusic_bot?startgroup=true"),
                    InlineKeyboardButton("▫️ᴍᴜsɪᴄ ʙᴏᴛ▫️", url="https://t.me/Olivia_xmusic_bot")
                ]                
            ]
        )
    )
