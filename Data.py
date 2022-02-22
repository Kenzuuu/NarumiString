from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Halo {}

My Name Is {}

I can help you retrieve the session string code.

    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("★ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ★", callback_data="generate")],
        [InlineKeyboardButton(text="★ ʙᴀᴄᴋ​ ★", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("★ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ★", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("★ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ★", callback_data="generate")],
        [InlineKeyboardButton("★ ᴍᴀɪɴᴛᴀɴᴇᴅ ʙʏ ​★", url="https://t.me/triplenineee")],
        [
            InlineKeyboardButton("★ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ ★​​", callback_data="help"),
            InlineKeyboardButton("★ ᴀʙᴏᴜᴛ​ ★", callback_data="about")
        ],
        [InlineKeyboardButton("★ ɪɴꜰo ʟᴀɪɴɴʏᴀ ​★", url="https://t.me/kenzusupport")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - Tentang Bot ini
/help - This Message
/start - Mulai Bot
/generate - Mulai Generating Session
/cancel - Membatalkan process
/restart - Membatalkan process
"""

    # About Message
    ABOUT = """
**About This Bot** 

Sebuah telegram bot untuk mengambil pyrogram dan telethon string session by @ZhuXstringBot

Group Support : [JOIN](https://t.me/Kenzusupport)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : [KENZHU](https://t.me/triplenineee)
    """
